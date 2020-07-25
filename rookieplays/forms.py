from django import forms

from .models import Topic

class TopicForm(forms.modelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
