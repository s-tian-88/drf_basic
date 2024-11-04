**[perimissions](https://www.django-rest-framework.org/api-guide/permissions/)**

**global settings**
```pytho
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```
**view settings**
``` python
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Note.objects.all()[:3]
        return Note.objects.filter(pk=pk)
    permission_classes = (IsAuthenticatedOrReadOnly, )
```

**custom permission**
```python
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
```
