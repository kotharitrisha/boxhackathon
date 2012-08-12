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
	del request.session['email']
	
	
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
                user = User.objects.get(email = data['email'])
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
