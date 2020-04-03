from django.shortcuts import render

from .models import Job
# Create your views here.
def home(Request):
	jobs = Job.objects
	return render(Request, 'jobs/home.html',{'jobs':jobs})