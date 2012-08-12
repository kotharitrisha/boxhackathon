from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import *
import ajax

def test(request):
	app_name = ajax.test(request)
	return render_to_response("test.html", app_name)

@csrf_exempt
def login(request):
	if(request.POST):
		print request.POST
		return HttpResponse("success")
	else:
		return render_to_response('login.html')

@csrf_exempt
def signup(request):
	if (request.POST):
		print request.POST
		return HttpResponse("successfully registered!")
	else:
		return render_to_response('signup.html')

@csrf_exempt
def edit(request):
	if (request.POST):
		print request.POST
		return HttpResponse("editted succesfully")
	else:
		return render_to_response('edit.html')
