from django import forms
from .models import List, Comment

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ('title', 'page_title', 'author', 'body',)

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'page_title': forms.TextInput(attrs={'class':'form-control'}),
			'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'yazan', 'type':'hidden'}),
			#'author': forms.Select(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ('title', 'page_title', 'body',)

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'page_title': forms.TextInput(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control'}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body',)



		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'yazanakq', 'type':'hidden'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type Your Comment....','label':'' })
		}	

	