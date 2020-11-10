# from vitrine.models import City, Country, Hotel, Vitrine
#
#
# class CityTable(table.Table):
#     class Meta(dashboard_table.Table.Meta):
#         model = City
#         fields = ['name', 'slug', 'state']
#
#
# class CountryTable(dashboard_table.Table):
#     class Meta(dashboard_table.Table.Meta):
#         model = Country
#         fields = ['name', 'slug']
#
#
# class HotelTable(dashboard_table.Table):
#     class Meta(dashboard_table.Table.Meta):
#         model = Hotel
#         fields = ['name', 'slug', 'image', 'city', 'country', 'category', 'price']
#
#
# class VitrineTable(dashboard_table.Table):
#     class Meta(dashboard_table.Table.Meta):
#         model = Vitrine
#         fields = ['title', 'subtitle', 'itens']