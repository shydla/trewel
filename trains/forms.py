from django import forms

from cities.models import City
from .models import Train


class HtmlForm(forms.Form):
    name = forms.CharField(label='Поезд')


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Поезд',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите номер поезда'}))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    travel_time = forms.IntegerField(label='Поезд',
                                     widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Время пути'}))

    class Meta(object):
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')
