from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Mentor, Feedback, Message, Event, LanguageSkill
from django.db.models import Q
from .forms import MentorForm
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(LOGIN_REDIRECT_URL)  # Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(LOGIN_REDIRECT_URL)  # Redirect after logout

# Fonction pour enregistrer un mentor
@login_required
def register_mentor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        year_of_study = request.POST.get('year_of_study')
        major = request.POST.get('major')
        nationality = request.POST.get('nationality')
        russian_language_level = request.POST.get('russian_language_level')

        # Création de l'utilisateur
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.save()

        # Création de l'enregistrement étudiant
        student = Student.objects.create(
            user=user,  # Lien avec l'utilisateur
            year_of_study=year_of_study,
            major=major,
            nationality=nationality,
            russian_language_level=russian_language_level
        )
        student.save()

        # Connexion de l'utilisateur après l'enregistrement
        login(request, user)
        return redirect('mentor_list')

    return render(request, 'register_mentor.html')

# Fonction pour afficher la liste des mentors
@login_required
def mentor_list(request):
    mentors = Mentor.objects.select_related('student__user').all()
    return render(request, 'mentor_list.html', {'mentors': mentors})

# Fonction pour gérer le chat
@login_required
def chat(request, receiver_id):
    # Get the receiver User instance
    receiver_user = get_object_or_404(User, id=receiver_id)

    # Get the corresponding Student instance for the receiver
    receiver_student = get_object_or_404(Student, user=receiver_user)

    if request.method == 'POST':
        content = request.POST.get('content')
        # Create a new message
        Message.objects.create(sender=request.user.student, receiver=receiver_student, content=content)
        return redirect('chat', receiver_id=receiver_id)

    # Fetch messages between the current user and the receiver
    messages = Message.objects.filter(
        Q(sender=request.user.student, receiver=receiver_student) |
        Q(sender=receiver_student, receiver=request.user.student)
    ).order_by('timestamp')

    return render(request, 'chat.html', {'receiver': receiver_user, 'messages': messages})

# Fonction pour gérer les retours d'expérience
@login_required
def feedback(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        student = Student.objects.get(user=request.user)
        Feedback.objects.create(student=student, message=message)
        return redirect('feedback')

    feedbacks = Feedback.objects.filter(student__user=request.user)
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

# Fonction pour afficher la liste des événements
@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

# Fonction pour créer un événement
@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Event.objects.create(title=title, description=description, date=date)
        return redirect('event_list')

    return render(request, 'create_event.html')

# Fonction pour ajouter une compétence linguistique
@login_required
def add_language_skill(request):
    if request.method == 'POST':
        language = request.POST.get('native_language')
        proficiency_level = request.POST.get('proficiency_level')

        # Obtention de l'étudiant actuel
        student = Student.objects.get(user=request.user)

        # Création d'une nouvelle compétence linguistique
        LanguageSkill.objects.create(student=student, native_language=language, proficiency_level=proficiency_level)
        return redirect('language_skill_list')  # Redirection après ajout
    return render(request, 'add_language_skill.html')

# Fonction pour afficher la liste des compétences linguistiques
@login_required
def language_skill_list(request):
    student = Student.objects.get(user=request.user)  # Obtention de l'étudiant actuel
    language_skills = LanguageSkill.objects.filter(student=student)
    return render(request, 'language_skill_list.html', {'language_skills': language_skills})

@login_required
def create_mentor(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new mentor record
            return redirect('mentor_list')  # Redirect to the mentor list after saving
    else:
        form = MentorForm()
    return render(request, 'create_mentor.html', {'form': form})

@login_required
def update_mentor(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id)
    if request.method == 'POST':
        form = MentorForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()  # Update the mentor record
            return redirect('mentor_list')  # Redirect to the mentor list after updating
    else:
        form = MentorForm(instance=mentor)
    return render(request, 'update_mentor.html', {'form': form, 'mentor': mentor})