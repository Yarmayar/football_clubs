from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import AddClubForm
from .models import Clubs, Country, TagClub

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add club', 'url_name': 'add_club'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Login', 'url_name': 'login'}
        ]


def index(request):
    clubs = Clubs.published.all().select_related('country')
    data = {
        'menu': menu,
        'title': 'Main Page',
        'clubs': clubs,
        'cntr_selected': 0,
    }
    return render(request, 'clubs/index.html', context=data)


def about(request):
    data = {
        'menu': menu,
        'title': 'About'
    }
    return render(request, 'clubs/about.html', data)


def show_club(request, club_slug):
    club = get_object_or_404(Clubs, slug=club_slug)

    data = {
        'menu': menu,
        'title': club.title,
        'club': club,
        'cntr_selected': None,
    }
    return render(request, 'clubs/club.html', data)


def add_club(request):
    if request.POST:
        form = AddClubForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    else:
        form = AddClubForm()
    context = {
        'menu': menu,
        'title': 'Adding new club',
        'form': form,
    }
    return render(request, 'clubs/addclub.html', context)


def feedback(request):
    return HttpResponse('Tell us what you want')


def login(request):
    return HttpResponse('Authorization form')


def show_country(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    clubs = Clubs.published.filter(country__slug=country_slug).select_related('country')
    data = {
        'menu': menu,
        'title': country.name,
        'clubs': clubs,
        'cntr_selected': country.id,
    }
    return render(request, 'clubs/index.html', context=data)


def show_tag_clubslist(request, tag_slug):
    tag = get_object_or_404(TagClub, slug=tag_slug)
    clubs = tag.tags.filter(is_published=Clubs.Status.PUBLISHED).select_related('country')
    context = {
        'menu': menu,
        'title': f'Tag: {tag.tag}',
        'clubs': clubs,
        'cntr_selected': None,
    }
    return render(request, 'clubs/index.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>This page can't be reached</h1>")
