from django.http import HttpResponse
from django.views.decorators.csrf import *
import sys
from models import *
import json

def test(request):
	return HttpResponse(json.dumps({'app_name': 'Trisha and the Trees'}))
	
@csrf_exempt
def login(request):
	res = {}
	try:
		data = request.POST.copy()
		user = User.objects.get(email = data['email'])
		if(user.password == data['password']):
			res['status']= True
		else:
			res['status']= False
	except:
		print sys.exc_info()[0]
		res['status']=False
	return res
	
	
@csrf_exempt
def register(request):
	res = {}
	try:
		data = request.POST.copy()
		user = User(email = data['email'], password= data['password'])
		user.save()
		res['status']= True
	except:
		print sys.exc_info()[0]
		res['status']=False
	return res
	
@csrf_exempt
def edit(request):
	pass
