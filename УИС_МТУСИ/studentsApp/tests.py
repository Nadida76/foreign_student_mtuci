from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student, Mentor, Feedback

class MentorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(
            first_name='Иван',
            last_name='Иванов',
            year_of_study=2,
            major='Информатика',
            nationality='Россия',
            russian_language_level='Средний'
        )
        self.mentor = Mentor.objects.create(
            student=self.student,
            schedule='Пн, Ср, Пт',
            comments='Опытный наставник'
        )

    def test_mentor_creation(self):
        self.assertEqual(self.mentor.student.first_name, 'Иван')
        self.assertEqual(self.mentor.schedule, 'Пн, Ср, Пт')

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(
            first_name='Иван',
            last_name='Иванов',
            year_of_study=2,
            major='Информатика',
            nationality='Россия',
            russian_language_level='Средний'
        )
        self.feedback = Feedback.objects.create(
            student=self.student,
            message='Отличный наставник!'
        )

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.message, 'Отличный наставник!')
        self.assertEqual(self.feedback.student.first_name, 'Иван')
