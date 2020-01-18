from django.shortcuts import render
import vk

def post(request):
    ACCESS_TOKEN ='eedebcb815835bd33a74a353fe60d525ae13dc940fe2998c3744a8021f5cd4c075160e48636eb0224c548'
    vkapi = vk.API(vk.Session(ACCESS_TOKEN))
    vkapi.wall.post( message='хуи', v=5.92)
    return(request)
