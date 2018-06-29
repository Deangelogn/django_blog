from django import forms
from .models import Post, Participant, Input

TYPE_SELECT = (
    ('1', 'Unfriendly'),
    ('2', ''),
    ('3', ''),
    ('4', ''),
    ('5', 'Friendly'),
)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class QuestionnaireForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('participant_name', 'participant_age')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'blog/horizontal_select.html'


class InputForm(forms.ModelForm):

    type_select =\
        forms.ChoiceField(choices=TYPE_SELECT, initial=0,
                          widget=HorizontalRadioSelect)

    # forms.ChoiceField(
    #     choices=TYPE_SELECT, initial=0,
    #     widget=forms.RadioSelect(attrs={'class': 'inline'}),
    #     )

    class Meta:
        model = Input
        fields = ['waist', 'height', 'type_select']

    # class Meta:
    #     model = Input
    #     gender = forms.ChoiceField(choices=GENDER_CHOICES,
    #                                widget=forms.RadioSelect())
    #     fields = {'waist', 'height', 'gender'}
