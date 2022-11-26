from .models import City, Metcast

from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'forms-control',
                                            'name': 'city',
                                            'id':'city',
                                            'placeholder':'Введите город'})}

class MetcastForm(ModelForm):
    class Meta:
        model = Metcast
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'forms-control',
                                            'name': 'city',
                                            'id':'city',
                                            'placeholder':'Введите город'})}