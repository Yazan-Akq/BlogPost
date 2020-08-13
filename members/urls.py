from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
     path('register/', views.register_user, name='register'),
     path('Edit_Profile/', views.EditProfile, name='Edit_Profile'),
     path('edit_password/', views.edit_password, name='edit_password'),

]
