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
