from cleanWorld.models import contactus, reports
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from hcaptcha.fields import hCaptchaField

from .models import User


class ProfileForm(forms.ModelForm):
	def  __init__(self, *args, **kwargs):

		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['username'].help_text = None
		self.fields['username'].disabled = True
		self.fields['email'].disabled = True
		self.fields['email'].label = 'ایمیل'

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = "form-control p-2 border-3"

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']


class SignupForm(UserCreationForm):
	hcaptcha = hCaptchaField()
	email = forms.EmailField(max_length=200)    
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
	hcaptcha = hCaptchaField()
	class Meta:
		model = User
		fields = '__all__'


class ContactForm(forms.ModelForm):
	# hcaptcha = hCaptchaField()
	class Meta:
		model = contactus
		fields = '__all__'


class ReportsForm(forms.ModelForm):
	def  __init__(self, *args, **kwargs):

		super(ReportsForm, self).__init__(*args, **kwargs)
		self.fields['garbageType'].label = 'نوع آلودگی'

	class Meta:
		model = reports
		fields = ('address', 'coordinates', 'garbageType')
