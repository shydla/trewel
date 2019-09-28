from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import City
from .forms import HtmlForm


def home(request):
    if request.method == 'POST':
        form = HtmlForm(request.POST or None)
    # print(request.POST)
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': cities, 'form': form})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'
