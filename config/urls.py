from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from note.views import NoteViewSet


router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('session-auth/', include('rest_framework.urls')),
]
