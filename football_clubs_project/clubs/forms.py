from django import forms
from .models import Country, Coach


class AddClubForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Content')
    is_published = forms.BooleanField(required=False, initial=True, label='Do release')
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Choose country')
    coach = forms.ModelChoiceField(queryset=Coach.objects.all(), required=False, empty_label='Vacancy')
