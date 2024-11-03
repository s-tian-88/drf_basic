from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

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
