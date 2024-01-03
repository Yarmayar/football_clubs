from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

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


class ShowClub(DetailView):
    # model = Clubs
    template_name = 'clubs/club.html'
    slug_url_kwarg = 'club_slug'
    # pk_url_kwarg = 'pk'  # изначально поиск объекта идет или по slug, или по pk,
    # если как у нас др имя переменной, то вносим его или здесь, или для слага - slug_url_kwarg
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['club'].title
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):  # для контроля получения только отвечающего критериям объекта (published) или 404
        return get_object_or_404(Clubs.published, slug=self.kwargs[self.slug_url_kwarg])


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
