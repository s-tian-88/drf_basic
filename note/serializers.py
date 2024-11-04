from rest_framework import serializers
from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Note
        fields = ('title', 'content', 'tag', 'user')

