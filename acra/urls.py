#!/usr/bin/env python
#encoding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'acra.views.dashboard', name='dashboard'),
	url(r'dashboard/', 'acra.views.dashboard', name='dashboard'),
	url(r'timeline/', 'acra.views.timeline', name='timeline'),
	url(r'_design/acra-storage/_update/report/', 'acra.views.index', name='submit'),
	
)
