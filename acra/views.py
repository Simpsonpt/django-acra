from api.decorators import only_post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from acra.models import CrashReport
import json

DEBUG = false
SESSION_NAME = "app_session"

#If there is no handling of the CSRF Token
#@csrf_exempt
def index(request):
	if(request.method=="POST"):
		description = ""
		if(request.POST.has_key("description")):
			description = request.POST["description"]
		notallow = ["description","solved",SESSION_NAME]
		crashreport= CrashReport()
		for key in request.POST:
			if (DEBUG):
				print "Key: %s in POST" % (key)
			if(not key.lower() in notallow):
				if(getattr(crashreport,key.lower(),None)!=None):
					if(DEBUG):
						print "ADDING %s -> %s" % (key.lower(),request.POST[key])
					v = getattr(crashreport,key.lower(),None)
					if(v!=None):
						setattr(crashreport,key.lower(),request.POST[key])
		crashreport.save()
		return HttpResponse(json.dumps({"id":crashreport.id}), content_type="application/json")
