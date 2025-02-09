from django.apps import AppConfig
from django.http import HttpResponse

class UserInfoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_info_app'


def user_info_view(request):
    return HttpResponse("User Info View works correctly!")
