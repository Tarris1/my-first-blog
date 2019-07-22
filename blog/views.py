from django.shortcuts import render

# Create your views here.

def post_list(request):
	return render(request,'blog/post_list.html',{}) #Render puts together the template blog/post_list.html




