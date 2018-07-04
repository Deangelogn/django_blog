from django import forms
from .models import Post, Questionnaire

EXTRAVERSION_OPTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

NEUROTICISM_OPTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

AGREEABLENESS_OPTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'blog/horizontal_select.html'


class QuestionnaireForm(forms.ModelForm):

    extraversion =\
        forms.ChoiceField(choices=EXTRAVERSION_OPTION, initial=0,
                          widget=HorizontalRadioSelect, label='')

    neuroticism =\
        forms.ChoiceField(choices=NEUROTICISM_OPTION, initial=0,
                          widget=HorizontalRadioSelect, label='')

    agreeableness =\
        forms.ChoiceField(choices=AGREEABLENESS_OPTION, initial=0,
                          widget=HorizontalRadioSelect, label='')

    class Meta:
        model = Questionnaire
        fields = ['extraversion', 'neuroticism', 'agreeableness']

# class InputForm(forms.ModelForm):
#
#     type_select =\
#         forms.ChoiceField(choices=TYPE_SELECT, initial=0,
#                           widget=HorizontalRadioSelect)
#
#     class Meta:
#         model = Input
#         fields = ['waist', 'height', 'type_select']

    # class Meta:
    #     model = Input
    #     gender = forms.ChoiceField(choices=GENDER_CHOICES,
    #                                widget=forms.RadioSelect())
    #     fields = {'waist', 'height', 'gender'}
