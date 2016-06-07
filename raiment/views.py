from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'raiment/index.html')

def community(request):
	return render(request, 'raiment/community.html')


def mood(request):
	return render(request, 'raiment/mood.html')
