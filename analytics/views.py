from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Public
from .serializers import PublicSerializer
from django.shortcuts import render

class PublicViewSet(viewsets.ModelViewSet):
    serializer_class = PublicSerializer
    queryset = Public.objects.all()

    def list(self, request):
        queryset = Public.objects.all()
        serializer = PublicSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Public.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PublicSerializer(token)
        return Response(serializer.data)

class SinglePublicView(RetrieveUpdateDestroyAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer
