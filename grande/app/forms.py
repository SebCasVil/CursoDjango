from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'pub_date': forms.HiddenInput(),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            # 'pub_date': forms.DateInput(attrs={'type': 'number'}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']