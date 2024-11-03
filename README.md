# Serializer

```python
# ./serializers.py
from rest_framework import serializers

from note.models import Note

class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_done = serializers.BooleanField(default=False)
    tag_id = serializers.IntegerField()

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.tag_id = validated_data.get('tag_id', instance.tag_id)
        instance.is_done = validated_data.get('is_done', instance.is_done)
        instance.save()
        return instance
```
```python
# ./views.py

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
```
