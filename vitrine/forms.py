from django import forms
from vitrine.models import City, Country, Hotel, Vitrine


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'


class VitrineForm(forms.ModelForm):
    class Meta:
        model = Vitrine
        fields = '__all__'