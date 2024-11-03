# Basic APIView

```python
class NoteAPIView(APIView):
    def get(self, request):
        lst = Note.objects.all().values()
        return Response({'title': list(lst)})

    def post(self, request):
        note_new = Note.objects.create(
                        title=request.data['title'],
                        content=request.data['content'],
                        tag_id=request.data['tag_id']
                    )
        return Response({'post': model_to_dict(note_new)})
```
