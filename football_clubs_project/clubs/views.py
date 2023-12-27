from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from clubs.models import Clubs

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add club', 'url_name': 'add_club'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Login', 'url_name': 'login'}
        ]
data_db = [
    {'id': 1, 'title': 'Zenit', 'content': 'info_zenit', 'is_published': True},
    {'id': 2, 'title': 'Liverpool', 'content': 'info_liverpool', 'is_published': True},
    {'id': 3, 'title': 'Monaco', 'content': 'info_monaco', 'is_published': True},
]

cntr_db = [
    {'id': 1, 'name': 'Russian'},
    {'id': 2, 'name': 'European'},
    {'id': 3, 'name': 'American'},
]


def index(request):
    clubs = Clubs.objects.filter(is_published=1)
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
        'cntr_selected': 0,
    }
    return render(request, 'clubs/club.html', data)


def add_club(request):
    return HttpResponse('Add new club')


def feedback(request):
    return HttpResponse('Tell us what you want')


def login(request):
    return HttpResponse('Authorization form')


def show_country(request, cntr_id):
    data = {
        'menu': menu,
        'title': 'Main Page',
        'clubs': data_db,
        'cntr_selected': cntr_id,
    }
    return render(request, 'clubs/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>This page can't be reached</h1>")
