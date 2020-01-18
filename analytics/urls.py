from django.contrib import admin
from django.urls import path,include
from . import views
from .views import PublicViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'public', PublicViewSet, basename='public')
urlpatterns = router.urls
