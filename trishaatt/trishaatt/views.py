from django.http import HttpResponse
import ajax

def test(request):
	app_name = ajax.test(request)
	return HttpResponse("Hello, Trisha and The Trees!" + str(app_name))
