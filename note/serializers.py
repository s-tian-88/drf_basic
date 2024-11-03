import io
from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class NoteModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

def encode():
    model = NoteModel('note title', 'note content')
    model_sr = NoteSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title":"note title","content":"note content"}')
    data = JSONParser().parse(stream)
    serialize = NoteSerializer(data=data)
    serialize.is_valid()
    print(serialize.validated_data)
    
