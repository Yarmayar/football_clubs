from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return HttpResponse('<h1> Main page</h1>')


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
