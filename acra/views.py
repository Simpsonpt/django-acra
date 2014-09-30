
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from acra.models import CrashReport
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.db import connection
from django.contrib.auth.decorators import login_required

import json
import logging

log = logging.getLogger("acra")
DEBUG = True
SESSION_NAME = "app_session"

#If there is no handling of the CSRF Token
@csrf_exempt
def index(request):
	
	
	if(request.method=="PUT" or request.method=="POST"):
		#log.log(logging.DEBUG, "got put "+ str(request.body) )
		json_data = json.loads(request.body)
		description = "";
		if(json_data.has_key("description")):
			description = json_data["description"]
		
		DEBUG = json_data['APP_VERSION_CODE'] == 10509999
		if DEBUG:
			log.log(logging.DEBUG, "REQUEST:: %s"%json_data['APP_VERSION_CODE'])
				
		
		notallow = ["description","solved",SESSION_NAME]
		crashreport= CrashReport()
		for key in json_data.keys():
			#if (DEBUG):
			#	log.log(logging.DEBUG, "Key: %s in POST" % (key) )
			if(not key.lower() in notallow):
				if(getattr(crashreport,key.lower(),None)!=None):
					#if(DEBUG):
					#	log.log(logging.DEBUG, "ADDING %s -> %s" % (key.lower(),json_data[key]) )
					v = getattr(crashreport,key.lower(),None)
					if(v!=None):
						setattr(crashreport,key.lower(),json_data[key])
		crashreport.save()
	
	return HttpResponse(json.dumps({"ok":"true"}), content_type="application/json")
		

@csrf_exempt
@login_required
def dashboard(request):
	android_versions = CrashReport.objects.filter().order_by("android_version").values("android_version").distinct();
	version_count = CrashReport.objects.filter().values('android_version').annotate(count=Count('pk')).order_by("android_version")
	app_version_count = CrashReport.objects.filter().values('app_version_name').annotate(count=Count('pk')).order_by("app_version_name")
	brand_count = CrashReport.objects.filter().values('brand').annotate(count=Count('pk')).order_by("brand")
	#log.log(logging.DEBUG, "query: "+str(app_version_count.query))

	return render(request, 'dashboard.html', {'android_verions': android_versions, 
											'versions':version_count,
											'app_version':app_version_count,
											'brand':brand_count})
	
	
@csrf_exempt
@login_required
def timeline(request):

	query = """
	select count(id) as count, date_format(created, '%Y-%m-%dT%H:00:00.0000') as datef from acra_crashreport
	group by datef
	order by datef
	"""
	cursor = connection.cursor()
	cursor.execute(query)
	data = cursor.fetchall();
	

	return render(request, 'timeline.html', {"time_data": data})
	
