from django import forms
from .models import Country, Coach


class AddClubForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    coach = forms.ModelChoiceField(queryset=Coach.objects.all(), required=False)
