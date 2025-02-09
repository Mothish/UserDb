from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_info_app.urls')),  # Include app URLs for cleaner organization
]
