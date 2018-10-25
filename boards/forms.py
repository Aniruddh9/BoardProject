from django import forms
from .models import Topic
from .models import Post

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name your thought'}),
        max_length=100)

    message = forms.CharField(
        widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='Max of 4000 characters can be entered.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
