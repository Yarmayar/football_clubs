import string

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Country, Coach


@deconstructible
class EnglishValidator:
    ALLOWED_CHARS = string.ascii_letters + string.digits + '-'
    code = 'english'

    def __init__(self, message=None):
        self.message = message if message else 'Only English letters, numbers, dashes and spaces must be present'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddClubForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5, label='Title', widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={
                                'min_length': 'too short title',
                                'required': 'No way without title',
                            })
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=[
                               MinLengthValidator(5, message='No less than 5 symbols'),
                               EnglishValidator(),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Content')
    is_published = forms.BooleanField(required=False, initial=True, label='Do release')
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Choose country')
    coach = forms.ModelChoiceField(queryset=Coach.objects.all(), required=False, empty_label='Vacancy')

    def clean_title(self):
        title = self.cleaned_data['title']
        allowed_chars = string.ascii_letters + string.digits + '-'

        if not (set(title) <= set(allowed_chars)):
            raise ValidationError('Only English letters, numbers, dashes and spaces must be present')
        return title