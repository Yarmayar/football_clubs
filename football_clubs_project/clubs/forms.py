import string

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Country, Coach, Clubs


@deconstructible
class EnglishValidator:
    ALLOWED_CHARS = string.ascii_letters + string.digits + '-'
    code = 'english'

    def __init__(self, message=None):
        self.message = message if message else 'Only English letters, numbers, dashes and spaces must be present'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddClubForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Choose country')
    coach = forms.ModelChoiceField(queryset=Coach.objects.all(), required=False, empty_label='Vacancy')

    class Meta:
        model = Clubs
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'is_published', 'country', 'tags', 'coach']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 75:
            raise ValidationError('Title field is longer than 75 characters')

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Club_logo')