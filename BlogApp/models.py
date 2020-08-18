from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class List(models.Model):
	title = models.CharField(max_length=255)
	page_title= models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body= models.TextField()
	Post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('home')
		
class Comment(models.Model):
	post = models.ForeignKey(List, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

	def get_absolute_url(self):
		return reverse('home')