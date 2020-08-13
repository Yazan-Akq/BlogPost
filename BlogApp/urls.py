from django.urls import path
from . import views
from .views import AddPostView, PostDetialView, EditView

urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('PostDetail/<int:pk>', PostDetialView.as_view(), name='PostDetail'),
    path('delete/<list_id>', views.delete, name = 'delete'),
    path('edit/<int:pk>', EditView.as_view(), name = 'edit'),
]
