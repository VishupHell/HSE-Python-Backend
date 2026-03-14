"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include
from django.urls import path

from rest_framework import routers

from backend.views import UsersAPIViewSet, PostsAPIViewSet, CommentsAPIViewSet, signup_view, login_view

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register(r'users', UsersAPIViewSet)
router.register(r'posts', PostsAPIViewSet)
router.register(r'comments', CommentsAPIViewSet)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include(router.urls), name='api'),
]
