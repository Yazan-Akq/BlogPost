from django.urls import path
from . import views
from .views import AddPostView, EditView, CommentView

urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('PostDetail/<int:pk>', views.PostDetailView, name='PostDetail'),
    path('delete/<list_id>', views.delete, name = 'delete'),
    path('edit/<int:pk>', EditView.as_view(), name = 'edit'),
    path('your_posts/', views.your_posts, name='your_posts'),
	path('PostDetail/Comment/<int:pk>', CommentView.as_view(), name='add_comment'),
	path('About/', views.about, name='about'),
	path('Contact/', views.contact, name='contact'),








]