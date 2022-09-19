from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from main.views import ProjectsViewSet

router = DefaultRouter()
router.register(r'projects', ProjectsViewSet, basename="projects")

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
