from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import UserFeedBack
# Create your views here.

def index(request):
	try:
		return render(request,'index.html')
	except:
		return render(request,'404.html')



def getuserfeedbackform(request):
	try:
		return render(request,'userfeedbackform.html')
	except:
		return render(request,'404.html')
		

def saveuserfeedbackform(request):
	try:
		obj = UserFeedBack()
		obj.title = request.GET['usertitle']
		obj.description = request.GET['userdescription']
		obj.save()
		mydict = {
		"feedback" : True
		}
		return render(request,'userfeedbackform.html',context=mydict)
	except:
		return render(request,'404.html')


