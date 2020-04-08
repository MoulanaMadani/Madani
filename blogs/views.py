from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(Request):
	blogs= Blog.objects 
	return render(Request, 'blogs/allblogs.html', {'blogs':blogs})

def details(Request, blog_id):
	blog_details= get_object_or_404(Blog, pk=blog_id)
	return render(Request, 'blogs/details.html', {'blog':blog_details})