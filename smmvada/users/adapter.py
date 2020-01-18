from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/rest-auth/user/{id}/{username}/{fn}/{ln}"
        return path.format(id=request.user.id,username=request.user.username,fn=request.user.first_name,ln=request.user.last_name)


