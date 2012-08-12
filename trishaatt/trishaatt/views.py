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
			return HttpResponseRedirect('/index')
		else:
			return HttpResponseRedirect('/login')			
	else:
		return render_to_response('login.html')

@csrf_exempt
def signup(request):
	if (request.POST):
		res = json.loads(ajax.register(request))
		if(res['status']):
			return HttpResponseRedirect("/index")
		else:
			return HttpResponseRedirect("/signup")
	else:
		return render_to_response('signup.html')


@csrf_exempt
def logout(request):
	ajax.logout(request)
	return HttpResponseRedirect('/login')	



@csrf_exempt
def edit(request):
	if (request.POST):
		print request.POST
		ajax.edit(request)
		return HttpResponse("editted succesfully")
	else:
		return render_to_response('edit.html')
		
		
@csrf_exempt
def project_add(request):
	if (request.POST):
		res = json.loads(ajax.project_add(request))
		print res
		if (res['status']):
			return HttpResponseRedirect("index.html")
		else:
			return HttpResponseRedirect("project_add.html")
	else:
		return render_to_response("project_add.html")
	
@csrf_exempt
def project_search(request):
	pass
	

@csrf_exempt
def project_edit(request):
	pass
	
@csrf_exempt
def project_delete(request):
	pass
	
	
@csrf_exempt
def task_add(request):
	pass
	
@csrf_exempt
def task_search(request):
	pass
	

@csrf_exempt
def task_edit(request):
	pass
	
@csrf_exempt
def task_delete(request):
	pass
