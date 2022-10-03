from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from main.views import ProjectsViewSet, CategoryViewSet, ApiViewSet, CaseViewSet

router = DefaultRouter()
router.register(r'projects', ProjectsViewSet, basename="projects")
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'apis', ApiViewSet, basename="apis")
router.register(r'cases', CaseViewSet, basename="cases")

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
