from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Связь с моделью User
    year_of_study = models.IntegerField()
    major = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    russian_language_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class LanguageSkill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    native_language = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50)
    has_certificate = models.BooleanField(default=False)

class Mentor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.TextField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.schedule}"

class Message(models.Model):
    sender = models.ForeignKey(Student, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Student, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    participants = models.ManyToManyField(Student)

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


