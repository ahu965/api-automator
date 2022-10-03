from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Project, Category, Api, Case


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']


class ProjectsSerializer(ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Project
        fields = ['id', 'name', 'desc', 'created_by', 'created_at']


class CategorySerializer(ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    type = serializers.CharField(default="collection", read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'parent_category', 'created_at']


class ApiSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    type = serializers.CharField(default="api", read_only=True)

    class Meta:
        model = Api
        fields = ['id', 'name', 'type', 'desc', 'method', 'path', 'params', 'headers', 'body', 'category', 'created_at']


class CaseSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Case
        fields = ['id', 'name', 'desc', 'method', 'path', 'params', 'headers', 'body', 'created_at']
