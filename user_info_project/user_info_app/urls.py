from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.user_info_view, name='index'),
      path('index/', views.user_info_view, name='index'),  # Home page with form handling
    path('get_data/', views.get_data, name='get_data'),  # Data listing page
    path('user_info/', views.user_info_view, name='user_info'),  # User info form page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('admin/', admin.site.urls),
    path('delete/', views.delete_users, name='delete_users'),
    path('update/<int:user_id>/', views.update_user, name='update_user'), 
    #path('', include('user_info_app.urls')),
    #path('data-list/', views.data_list_view, name='data_list'),

]
