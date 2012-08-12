from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import *
import ajax, json

def index(request):
	try:
		#c = RequestContext(request, {'email': request.session['email']})
		return render_to_response("index.html")		
	except:
		return render_to_response("login.html")
		
		

@csrf_exempt
def login(request):
	if(request.POST):
		res = json.loads(ajax.login(request))
		if(res['status']):
			return HttpResponseRedirect('index.html')
		else:
			return HttpResponseRedirect('login.html')			
	else:
		return render_to_response('login.html')

@csrf_exempt
def signup(request):
	if (request.POST):
		res = json.loads(ajax.register(request))
		if(res['status']):
			return HttpResponseRedirect("index.html")
		else:
			return HttpResponseRedirect("register.html")
	else:
		return render_to_response('signup.html')


@csrf_exempt
def logout(request):
	ajax.logout(request)
	return HttpResponseRedirect('login.html')	



@csrf_exempt
def edit(request):
	if (request.POST):
		print request.POST
		ajax.edit(request)
		return HttpResponse("editted succesfully")
	else:
		return render_to_response('edit.html')
