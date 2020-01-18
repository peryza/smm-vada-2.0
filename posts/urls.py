from django.contrib import admin
from django.urls import path,include
from . import views
from .views import PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
urlpatterns = [
    path('go/', views.post, name='post'),

]
urlpatterns += router.urls
