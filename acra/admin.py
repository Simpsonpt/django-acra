from django.contrib import admin
from django.contrib.auth.models import User
from acra.models import *

def statusUpdate(self, request, queryset):
	rows_updated = queryset.update(solved='solved')
	if rows_updated == 1:
		message_bit = "One Report was"
	else:
		message_bit = "%s Reports were" % rows_updated
	self.message_user(request, "%s successfully marked as Solved." % message_bit)
statusUpdate.short_description = "Mark selected report(s) as solved"

class CrashReportAdmin(admin.ModelAdmin):
	fieldsets = [
		('Application Information', {'fields':['app_version_name','app_version_code','package_name']}),
		('Report Status', {'fields': ['description','solved'],'description': "Useful information to fix this issue."}),
		('Base Information', {'fields':['report_id','installation_id','brand','product','phone_model','android_version','user_app_start_date','user_crash_date','created'],'classes': ['collapse']}),
		('Crash Data', {'fields':['logcat','stack_trace','environment','shared_preferences','total_mem_size','available_mem_size','dumpsys_meminfo','initial_configuration','file_path','crash_configuration'],'classes': ['collapse']}),
		('Device', {'fields':['build','display','settings_global','settings_system','settings_secure','device_features'],'classes': ['collapse']}),
		('Special Information', {'fields':['user_email','is_silent','user_comment','custom_data'],'classes': ['collapse']})
	]
	list_display = ('brand','product','android_version','created','app_version_name','solved')
	readonly_fields = ('report_id','installation_id','brand','product','phone_model','android_version','user_app_start_date','user_crash_date','created','app_version_name','app_version_code','package_name','logcat','stack_trace','environment','shared_preferences','total_mem_size','available_mem_size','dumpsys_meminfo','initial_configuration','file_path','crash_configuration','build','display','settings_global','settings_system','settings_secure','device_features','user_email','is_silent','user_comment','custom_data')
	list_filter = ['brand','solved','android_version','app_version_code','created']
	search_fields = ['brand','product','description']
	actions = [statusUpdate]
		
admin.site.register(CrashReport, CrashReportAdmin)
