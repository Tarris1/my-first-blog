from django.shortcuts import render
from django.utils import timezone
from .models import Post #. in same directory
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts': posts}) #Render puts together the template blog/post_list.html
	#Request -> everything received from user via internet



