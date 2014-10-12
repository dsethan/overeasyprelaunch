from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def home(request):
	context = RequestContext(request)

	return render_to_response(
		'prelaunch_home.html',
		{},
		context)

def menu(request):
	context = RequestContext(request)

	return render_to_response(
		'prelaunch_menu.html',
		{},
		context)