from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView

from .forms import AddClubForm, UploadFileForm
from .models import Clubs, Country, TagClub, UploadFiles

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add club', 'url_name': 'add_club'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Login', 'url_name': 'login'}
        ]


class ClubsHome(ListView):
    # model = Clubs
    template_name = 'clubs/index.html'
    context_object_name = 'clubs'  #  по умолчанию список объектов модели содержится в self.object_list
    extra_context = {
        'menu': menu,
        'title': 'Main Page',
        'cntr_selected': 0,
    }

    def get_queryset(self):  # для получения кастомиз списка объектов модели (стат опубликовано)
        return Clubs.published.all().select_related('country')


def about(request):
    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_object = UploadFiles(file=form.cleaned_data['file'])
            file_object.save()

    else:
        form = UploadFileForm()
    data = {
        'menu': menu,
        'title': 'About',
        'form': form,
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


class AddClub(View):
    def get(self, request):
        form = AddClubForm()
        context = {
            'menu': menu,
            'title': 'Adding new club',
            'form': form,
        }
        return render(request, 'clubs/addclub.html', context)

    def post(self, request):
        form = AddClubForm(request.POST, request.FILES)
        if form.is_valid():
            redirect('home')
            form.save()
        return redirect('home')


def feedback(request):
    return HttpResponse('Tell us what you want')


def login(request):
    return HttpResponse('Authorization form')


# def show_country(request, country_slug):
#     country = get_object_or_404(Country, slug=country_slug)
#     clubs = Clubs.published.filter(country__slug=country_slug).select_related('country')
#     data = {
#         'menu': menu,
#         'title': country.name,
#         'clubs': clubs,
#         'cntr_selected': country.id,
#     }
#     return render(request, 'clubs/index.html', context=data)


class ClubsCountry(ListView):
    template_name = 'clubs/index.html'
    context_object_name = 'clubs'
    allow_empty = False  # при пустом списке объектов (напр несуществующий country_slug) будет генерироваться ошибка 404

    def get_queryset(self):
        return Clubs.published.filter(country__slug=self.kwargs['country_slug']).select_related('country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = context['clubs'][0].country
        context['title'] = 'Clubs of ' + country.name
        context['menu'] = menu
        context['cntr_selected'] = country.pk
        return context


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


class ClubsTag(ListView):
    template_name = 'clubs/index.html'
    context_object_name = 'clubs'
    allow_empty = False

    def get_queryset(self):
        return Clubs.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagClub.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = f'Tag: {tag}'
        context['menu'] = menu
        context['cntr_selected'] = None
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>This page can't be reached</h1>")
