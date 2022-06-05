from django import forms
from hiru.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question # 사용모델
        fields=['subject', 'content'] #사용할 모델 속성