from django.http import HttpResponse
import json

def test(request):
	return HttpResponse(json.dumps({'app_name': 'Trisha and the Trees'}))
