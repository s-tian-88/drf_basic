from django.contrib import admin
from django.urls import path

from note.views import NoteAPIView, NoteUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', NoteAPIView.as_view()),
    path('notes/<int:pk>/', NoteUpdateAPIView.as_view())
]
