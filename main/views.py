# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from main.filters import ProjectsFilter
from main.models import Projects
from main.serializer import ProjectsSerializer


class ProjectsViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Projects.objects.filter()
    serializer_class = ProjectsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectsFilter
