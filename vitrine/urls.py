from django.urls import path

from vitrine.apis import VitrineAPI
from vitrine.views import lista_vitrine, destinos_vitrine, sobre_vitrine, cadastro_cidades, cadastro_vitrine

urlpatterns = [
    path('lista/', lista_vitrine, name='vitrine-lista'),
    path('destinos/', destinos_vitrine, name='vitrine-destinos'),
    path('sobre/', sobre_vitrine, name='vitrine-sobre'),
    path('city/', cadastro_cidades, name='cadastro-cidades'),
    path('vitrine/', cadastro_vitrine, name='cadastro-vitrine'),

    path('api/', VitrineAPI.as_view(), name='api-vitrine')
]

