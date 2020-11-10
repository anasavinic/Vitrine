from rest_framework import status
from vitrine.models import Vitrine
from rest_framework.response import Response
from rest_framework.views import APIView

from vitrine.serializer import VitrineSerializer


class VitrineAPI(APIView):

    def get(self, request, format=None):
        vitrine = Vitrine.objects.all()
        serializer = VitrineSerializer(vitrine, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
