from django.http import HttpResponse
from django.views.decorators.csrf import *
import sys
from models import *
import json
import datetime

def test(request):
	return HttpResponse(json.dumps({'app_name': 'Trisha and the Trees'}))
	
@csrf_exempt
def login(request):
	res = {}
	try:
		data = request.REQUEST.copy()
		user = User.objects.get(email = data['email'])
		if(user.password == data['password']):
			request.session['email'] = data['email']
			res['status']= True
		else:
			res['status']= False
	except:
		print sys.exc_info()[0]
		res['status']=False
	return json.dumps(res)



@csrf_exempt
def logout(request):
	try:
		del request.session['email']
	except:
		pass
	
	
@csrf_exempt
def register(request):
	res = {}
	try:
		data = request.REQUEST.copy()
		user = User.objects.get(email = data['email'])
		res['status']= False				
	except User.DoesNotExist:
		try:		
			user = User(email = data['email'], password= data['password'])
			b = user.save()
			request.session['email'] = data['email']
			res['status']= True	
		except:
			res['status']= True	
	except:
		print sys.exc_info()[0]
		res['status']=False
	return json.dumps(res)



	
@csrf_exempt
def edit(request):
	res = {}
	try:
		data = request.POST.copy()
		user = User.objects.get(email = request.session['email'])
		if data["phone"]:
			user.phone= data["phone"]
		else:
			return
		b = user.save()
		print b
		res['status'] = True
	except:
			print sys.exc_info()[0]
			res['status']=False
	return res
	
@csrf_exempt
def project_add(request):
        res = {}
	try:
		data = request.REQUEST.copy()
       		today = datetime.datetime.today()
		print today
		user = User.objects.get(email = data['owner'])
		project = Project(title = data['title'], desc= data['desc'], filename = data['filename'], deadline = today, owner =user)
		project.save()
		res['status']= True
	except:
		print sys.exc_info()[0]
		res['status']= True
        return json.dumps(res)
	
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
	res = {}
        try:
		data = request.REQUEST.copy()
	        print data
                today = datetime.datetime.today()
                print today
                project = Project.objects.get(id = data['title'])
		user = project.owner
                task = Task(desc = data['desc'], step_id= data['step_id'],  step_deadline = today, project_id = project, owner =user)
                task.save()
                res['status']= True
        except:
                print sys.exc_info()[0]
                res['status']= False
        return json.dumps(res)
	
@csrf_exempt
def task_search(request):
	pass
	

@csrf_exempt
def task_edit(request):
	pass
	
@csrf_exempt
def task_delete(request):
	pass
	
