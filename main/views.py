# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from main.filters import ProjectsFilter
from main.models import Project, Category, Api, Case
from main.serializer import ProjectsSerializer, CategorySerializer, ApiSerializer, CaseSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.filter()
    serializer_class = ProjectsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectsFilter
    pagination_class = PageNumberPagination


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        query_params = self.request.query_params
        if 'parent_category' in query_params:
            if query_params['parent_category'] == '-1':
                return Category.objects.filter(parent_category__isnull=True)
            else:
                return Category.objects.filter(parent_category=query_params['parent_category'])
        else:
            return Category.objects.filter()


class ApiViewSet(ModelViewSet):
    queryset = Api.objects.filter()
    serializer_class = ApiSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.filter()
    serializer_class = CaseSerializer


class CategoryApiView(APIView):
    def get(self, request):
        category = None
        if "category" in request.GET:
            category = request.GET['category']
        if category:
            query_set = Category.objects.filter(parent_category=category)
            category_data = CategorySerializer(query_set, many=True).data
            query_set = Api.objects.filter(category=category)
            api_data = ApiSerializer(query_set, many=True).data
        else:
            query_set = Category.objects.filter(parent_category__isnull=True)
            category_data = CategorySerializer(query_set, many=True).data
            query_set = Api.objects.filter(category__isnull=True)
            api_data = ApiSerializer(query_set, many=True).data
        return Response(category_data + api_data)
