from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup(request):
	return render(request, 'registration/signup.html')

def create_user(request):
	new_username = request.POST.get('signup-username')
	new_password = request.POST.get('signup-password')
	new_email = request.POST.get('signup-email')

	user = User.objects.create_user(username= new_username,
                                 email= new_email,
                                 password= new_password)
	user.save()

	return render(request,'raiment/index.html')

@login_required
def index(request):
    return render(request, 'raiment/index.html')

def community(request):
	return render(request, 'raiment/community.html')


def mood(request):
	return render(request, 'raiment/mood.html')

