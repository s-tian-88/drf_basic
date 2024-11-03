# ModelSerializer

```python
# ./serialoizers.py
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content', 'tag')
```
```python
# ./view.py
class NoteAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
```
