from django.shortcuts import render, redirect, get_object_or_404
from .models import List,Comment
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import ListForm, EditForm, CommentForm
from django.contrib import messages
from django.urls import reverse_lazy

def home(request):
	form = List.objects.all().order_by('-id')
	context = {'form':form}
	return render(request, 'home.html', context)

class AddPostView(CreateView):
	model = List
	form_class = ListForm
	template_name = 'add_post.html'
	#fields = ('title', 'page_title', 'author', 'body',)

class PostDetialView(DetailView):
	model = List
	template_name = 'Detail.html'

def delete(request, list_id):
	form = List.objects.get(pk=list_id)
	form.delete()	
	messages.success(request, ('Post Has Been Deleted...'))
	return redirect('home')

class EditView(UpdateView):
	model = List
	form_class = EditForm
	template_name = 'edit.html'
	#fields = ('title', 'page_title', 'body',)

def your_posts(request):
	form = List.objects.all().order_by('-id')
	context = {'form':form}
	return render(request, 'your_posts.html', context)

class CommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)