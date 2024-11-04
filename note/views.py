from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Note.objects.all()[:3]
        return Note.objects.filter(pk=pk)
