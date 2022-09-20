"""apiAutomator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
# from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView

import main.urls

schema_view = get_schema_view(
    openapi.Info(
        title="「接口测试平台」文档",  # 必传
        default_version='v1',  # 必传
        description="接口文档",
        terms_of_service='',
        contact=openapi.Contact(email="huyptina@163.com"),
        license=openapi.License(name="BSD LICENSE")
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),

    path('admin/', admin.site.urls),

    # 登录
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('main/', include(main.urls)),
]
