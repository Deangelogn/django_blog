from django import forms

from .models import Post, Participant


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class Questionary(forms.ModelForm):
    model = Participant
