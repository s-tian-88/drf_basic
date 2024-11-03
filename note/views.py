from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response


class NoteAPIView(APIView):
    def get(self, request):
        lst = Note.objects.all()
        serialized = NoteSerializer(lst, many=True).data
        return Response({"notes": serialized})

    def post(self, request):
        print('request.data: ', request.data, '\n')
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() # вызывает метод create сериализатора
        print('serializer.data: ', serializer.data, '\n') # NoteSerializer.create => data
        return Response({'new note': serializer.data})

    def put(self, request, *args, **kwargs):
        # kwargs - коллекция параметров запроса
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Note.objects.get(pk=pk)
        except:
            return Response({"errror": "Object does not exists"})
        serializer = NoteSerializer(data=request.data, instance=instance)
        # При наличии двух аргументов - data, instance, вызывается матод NoteSerializer.update
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

