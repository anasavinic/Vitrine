from rest_framework.serializers import ModelSerializer

from vitrine.models import Vitrine


class VitrineSerializer(ModelSerializer):
    class Meta:
        model = Vitrine
        fields = ['id', 'title', 'subtitle', 'itens']