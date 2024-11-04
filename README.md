```python
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')
```

```python
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Note.objects.all()[:3]
        return Note.objects.filter(pk=pk)
```
