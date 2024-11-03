# Serializers

**base work example**
```python
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
```

**example**
```python
# ./serializers.py
class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_done = serializers.BooleanField(default=False)
    tag_id = serializers.IntegerField()
```
```python
# ./views.py
class NoteAPIView(APIView):
    def get(self, request):
        lst = Note.objects.all()
        serialized = NoteSerializer(lst, many=True).data
        return Response({"notes": serialized})

    def post(self, request):
        print(request.data)
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_obj = Note.objects.create(**serializer.validated_data)
        return Response({'new note': NoteSerializer(new_obj).data})
```
