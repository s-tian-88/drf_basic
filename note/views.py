from rest_framework.views import APIView # Базовый класс представления
from rest_framework.response import Response

from .models import Note

class NoteAPIView(APIView):
    def get(self, request):
        return Response({'title': 'get'})

    def post(self, request):
        return Response({'title': 'post'})

