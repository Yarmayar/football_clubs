from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddClubForm, UploadFileForm
from .models import Clubs, Country, TagClub, UploadFiles
from .utils import DataMixin


class ClubsHome(DataMixin, ListView):
    template_name = 'clubs/index.html'
    context_object_name = 'clubs'  #  по умолчанию список объектов модели содержится в self.object_list
    page_title = 'Main page'
    cntr_selected = 0

    def get_queryset(self):  # для получения кастомиз списка объектов модели (стат опубликовано)
        return Clubs.published.all().select_related('country')


def about(request):
    clubs_list = Clubs.published.all()
    paginator = Paginator(clubs_list, 4, orphans=3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    data = {
        'title': 'About',
        'page_object': page_object,
    }
    return render(request, 'clubs/about.html', data)


class ShowClub(DataMixin, DetailView):
    # model = Clubs
    template_name = 'clubs/club.html'
    slug_url_kwarg = 'club_slug'
    # pk_url_kwarg = 'pk'  # изначально поиск объекта идет или по slug, или по pk,
    # если как у нас др имя переменной, то вносим его или здесь, или для слага - slug_url_kwarg
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['club'].title)

    def get_object(self, queryset=None):  # для контроля получения только отвечающего критериям объекта (published) или 404
        return get_object_or_404(Clubs.published, slug=self.kwargs[self.slug_url_kwarg])


class AddClub(DataMixin, CreateView):
    template_name = 'clubs/addclub.html'
    form_class = AddClubForm # или связываем представление с формой, или указываем модель и отображ поля модели
    page_title = 'Adding new club'
    # model = Clubs
    # fields = '__all__'
    # success_url = reverse_lazy('home')


class UpdateClub(DataMixin, UpdateView):
    template_name = 'clubs/addclub.html'
    model = Clubs
    fields = ['title', 'content', 'logo', 'country', 'is_published', 'coach', 'tags']
    page_title = 'Edit club'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class DeleteClub(DataMixin, DeleteView):
    model = Clubs
    success_url = reverse_lazy('home')
    page_title = 'Delete club'


def feedback(request):
    return HttpResponse('Tell us what you want')


def login(request):
    return HttpResponse('Authorization form')


class ClubsCountry(DataMixin, ListView):
    template_name = 'clubs/index.html'
    context_object_name = 'clubs'
    allow_empty = False  # при пустом списке объектов (напр несуществующий country_slug) будет генерироваться ошибка 404

    def get_queryset(self):
        return Clubs.published.filter(country__slug=self.kwargs['country_slug']).select_related('country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = context['clubs'][0].country
        context['title'] = 'Clubs of ' + country.name
        context['cntr_selected'] = country.pk
        return self.get_mixin_context(context)


class ClubsTag(DataMixin, ListView):
    template_name = 'clubs/index.html'
    context_object_name = 'clubs'
    allow_empty = False

    def get_queryset(self):
        return Clubs.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagClub.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = f'Tag: {tag}'
        return self.get_mixin_context(context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>This page can't be reached</h1>")
