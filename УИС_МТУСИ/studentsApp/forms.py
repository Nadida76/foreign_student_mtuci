from django import forms
from .models import Feedback, Mentor


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['student', 'schedule', 'comments']