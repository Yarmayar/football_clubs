from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

menu = ['About', 'Add club', 'Feedback', 'Login']
data_db = [
    {'id': 1, 'title': 'Zenit', 'content': 'info_zenit', 'is_published': True},
    {'id': 2, 'title': 'Liverpool', 'content': 'info_liverpool', 'is_published': True},
    {'id': 3, 'title': 'Monaco', 'content': 'info_monaco', 'is_published': True},
]


def index(request):
    data = {
        'menu': menu,
        'title': 'Main Page',
        'posts': data_db
    }
    return render(request, 'clubs/index.html', context=data)


def about(request):
    data = {
        'manu': menu,
        'title': 'Main Page'
    }
    return render(request, 'clubs/about.html', data)


def countries(request, cntr_id):
    return HttpResponse(f'<h1> Main page</h1><p>Country id = {cntr_id}</p>')


def countries_by_slug(request, cntr_slug):
    return HttpResponse(f'<h1> Main page</h1><p>Country slug = {cntr_slug}</p>')


def archive(request, year):
    if 1991 <= year <= 2023:
        return HttpResponse(f'<h1> Main page</h1><p>Archive by year = {year}</p>')
    uri = reverse('countries', args=('portugal', ))
    return HttpResponsePermanentRedirect(uri)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>This page can't be reached</h1>")
