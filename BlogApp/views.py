from django.shortcuts import render, redirect
from .models import List
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import ListForm, EditForm
from django.contrib import messages

def home(request):
	form = List.objects.all()
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
	return redirect('home')

class EditView(UpdateView):
	model = List
	form_class = EditForm
	template_name = 'edit.html'
	#fields = ('title', 'page_title', 'body',)

