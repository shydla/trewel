from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from .models import City
from .forms import CityForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def home(request):
    # if request.method == 'POST':
    #     form = CityForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    # form = CityForm()
    # city = request.POST.get('name')
    # print(request.POST)

    cities = City.objects.all()
    paginator = Paginator(cities, 2)
    page = request.GET.get('page')
    objects_list = paginator.get_page(page)
    return render(request, 'cities/home.html', {'objects_list': objects_list})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно создан'


class CityDeleteView(DeleteView):
    model = City
#    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')

    def get(self, request, *args, **kwargs):
        messages.error(request, 'Город удален')
        return self.post(request, *args, **kwargs)


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')
    success_message = 'Город успешно отредактирован'
