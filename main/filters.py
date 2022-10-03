from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from main.models import Project


class ProjectsFilter(FilterSet):
    # 指定需要模糊查询的字段
    name = CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写

    class Meta:
        # 指定模型
        models = Project
        fields = ['name']
