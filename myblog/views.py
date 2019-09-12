from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader, Template
 
from myblog.models import story
#def Start(request):
	#return render(request,'loadinganimation.html')


def home(request):
	return render(request,'start.html')
def STORY(request):
--    return render(request, 'story.html', {'dastan': Story})




def Comment(request):
	return render(request, 'comment.html')


def Call(request):
	return render(request,'call.html')

def About(request):
	return render(request,'About.html')