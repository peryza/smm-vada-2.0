from django.contrib import admin
from django.urls import path,include
from . import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls
