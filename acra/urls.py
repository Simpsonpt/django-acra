#!/usr/bin/env python
#encoding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'acra.views.index', name='submit'),
)
