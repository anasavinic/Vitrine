# from vitrine.models import City, Country, Hotel, Vitrine
#
#
# class CityFilter(django_filters.FilterSet):
#     class Meta:
#         model = City
#         fields = ['name', 'state']
#
#
# class CountryFilter(django_filters.FilterSet):
#     class Meta:
#         model = Country
#         fields = ['name']
#
#
# class HotelFilter(django_filters.FilterSet):
#     class Meta:
#         model = Hotel
#         fields = ['name', 'city', 'country', 'category']
#
#
# class VitrineFilter(django_filters.FilterSet):
#     class Meta:
#         model = Vitrine
#         fields = ['title']