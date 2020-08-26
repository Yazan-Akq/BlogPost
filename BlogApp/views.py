from django.shortcuts import render, redirect, get_object_or_404
from .models import List,Comment
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import ListForm, EditForm, CommentForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

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

def about(request):
	return render(request, 'about.html')	

def contact(request):
	if request.method == 'POST':
		message_name = request.POST.get('message-name')
		message_email = request.POST.get('message-email')
		message = request.POST.get('message')

		send_mail(
			'message from ' + message_name + ' |email| ' + message_email,
			message,
			message_email,
			['yazanakq@gmail.com'],
		)

		return render(request, 'contact.html', {'message_name':message_name})	




	else:	
		return render(request, 'contact.html')	