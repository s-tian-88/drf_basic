from django.contrib import admin
from django.urls import path

from note.views import NoteAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', NoteAPIView.as_view())
]
