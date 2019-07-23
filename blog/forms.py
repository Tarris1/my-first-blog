from django import forms
from .models import Post

class PostForm(forms.ModelForm): #Name of our form and its a ModelForm

	class Meta: #Here we tell Django which model should be used to create this form
		model = Post
		fields = ('title','text',)

