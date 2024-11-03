from rest_framework import generics # набор базовых классов для представления

from .models import Note
from .serializers import NoteSerializer

class NoteAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
