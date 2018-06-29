from django import forms
from .models import Post, Participant, Input
from django.utils.safestring import mark_safe

TYPE_SELECT = (
    ('0', 'Live'),
    ('1', 'Test'),
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


class HorizontalRadioRenderer(forms.RadioSelect):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class InputForm(forms.ModelForm):

    type_select = forms.ChoiceField(widget=forms.RadioSelect(
                        renderer=HorizontalRadioRenderer), choices=TYPE_SELECT)

    class Meta:
        model = Input
        fields = ['waist', 'height', 'type_select']

    # class Meta:
    #     model = Input
    #     gender = forms.ChoiceField(choices=GENDER_CHOICES,
    #                                widget=forms.RadioSelect())
    #     fields = {'waist', 'height', 'gender'}
