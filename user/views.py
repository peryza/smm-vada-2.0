from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(token)
        return Response(serializer.data)

class SingleUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
