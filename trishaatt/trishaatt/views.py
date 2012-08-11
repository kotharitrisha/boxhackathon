from django.http import HttpResponse
from django.shortcuts import render_to_response
import ajax

def test(request):
	app_name = ajax.test(request)
	return render_to_response("test.html", app_name)
	


                                                                                                                            
