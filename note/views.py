from .models import Note, Tag
from .serializers import NoteSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Note.objects.all()[:3]
        return Note.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def tags(self, request):
        tags = Tag.objects.all()
        return Response({"tags": [t.title for t in tags]})

