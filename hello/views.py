from django.shortcuts import render
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, render


def hello(request):
	c = RequestContext(request, {
	})
	return render_to_response('hello/hello.html', c)