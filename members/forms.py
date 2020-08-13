from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = ''
		self.fields['username'].form = ''

		self.fields['password1'].widget.attrs['class'] = 'form-control'		
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = ''
		self.fields['password1'].form = ''

		self.fields['password2'].widget.attrs['class'] = 'form-control'		
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'		
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = ''
		self.fields['password2'].form = ''

class EditProfileForm(UserChangeForm):
	password = forms.CharField(label='', widget=forms.TextInput(attrs={'type': 'hidden'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email','password')


	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].help_text = ''
		self.fields['username'].form = ''			

class EditPasswordForm(PasswordChangeForm):
	class Meta:
		model = User
		fields = ('Old password', 'New password', 'New password confirmation',)

	def __init__(self, *args, **kwargs):
		super(EditPasswordForm, self).__init__(*args, **kwargs)

		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].help_text = ''
		self.fields['old_password'].form = ''	

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].help_text = ''
		self.fields['new_password1'].form = ''	

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].label = 'Confirm New Password'
		self.fields['new_password2'].help_text = ''
		self.fields['new_password2'].form = ''	

