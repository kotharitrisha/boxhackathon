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
		project = Project(title = data['title'], desc= data['desc'], filename = data['filename'])
		project.save()
		res['status']= True
		res['id']= project.id
	except:
		print sys.exc_info()[0]
		res['status']= False
	return HttpResponse(json.dumps(res))

	
@csrf_exempt
def project_search(request):
	try:
		res = {}
		res['projects'] = []		
		for p in Project.objects.all():
			res['projects'].append({'id': str(p.id), 'title': str(p.title), 'desc' : str(p.desc)})
		res['status'] = True
	except:
		print sys.exc_info()[0]
		res['status']= False
	return HttpResponse(json.dumps(res))
	

@csrf_exempt
def project_edit(request):
	pass
	
@csrf_exempt
def project_delete(request):
	res = {}
	try:
		data = request.REQUEST.copy()
		project = Project.objects.get(title = data['title'])
		project.delete()
	except:
		print sys.exc()[0]
        return json.dumps(res)
	
	
@csrf_exempt
def task_add(request):
	res = {}
	try:
		data = request.REQUEST.copy()
		print data
		today = datetime.datetime.today()
		project = Project.objects.get(id=2)
		user = User.objects.get(email = data['owner'])
		print "so it is reaching user?"
		task = Task(desc = data['desc'], step_id= 1,  step_deadline = today, project = project, owner =user)
		task.save()
		res['status']= True
	except:
		print sys.exc_info()[0]
		res['status']= False
	return HttpResponse(json.dumps(res))

	
@csrf_exempt
def task_search(request):
	res = {}
	res['tasks'] = []
	try:
		print "here..."
		data = request.REQUEST.copy()
		print data			
		task = Task.objects.filter(project_id = int(data['id']))
		print "I am here..."	
	
		for t in task:
			res['tasks'].append({'project_id': str(t.project.id), 'desc': str(t.desc), 'step_deadline' : str(t.step_deadline),
			'owner_id' : str(t.owner.id), 'step_id' : str(t.step_id)})

		res['status'] = True
		print "done..."
	except:
		print sys.exc_info()[0]
		res['status']= False
	return HttpResponse(json.dumps(res))
	

@csrf_exempt
def task_edit(request):
	pass
	
@csrf_exempt
def task_delete(request):
	res = {}
	try:
		data = request.REQUEST.copy()
		task = Task.objects.get(desc = data['desc'])
		task.delete()
		res['status'] = True
	except:
		print sys.exc()[0]
		res['status'] =False
	return json.dumps(res)
	
