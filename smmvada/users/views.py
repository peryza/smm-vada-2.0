from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
import vk

def post(request):
    ACCESS_TOKEN ='eedebcb815835bd33a74a353fe60d525ae13dc940fe2998c3744a8021f5cd4c075160e48636eb0224c548'
    vkapi = vk.API(vk.Session(ACCESS_TOKEN))
    vkapi.wall.post( message='хуи', v=5.92)
    return(request)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(token)
        return Response(serializer.data)

class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
