from django.shortcuts import render
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, render
from core.middleware import test1, Test2, Test3

@test1
def hello1(request):
    print ">>>>>>>view"
    c = RequestContext(request, { })
    return render_to_response('hello/hello.html', c)

@Test2
def hello2(request):
    print ">>>>>>>view"
    c = RequestContext(request, { })
    return render_to_response('hello/hello.html', c)

def hello3(request):
    print ">>>>>>>view"
    c = RequestContext(request, { })
    return render_to_response('hello/hello.html', c)

# @test2
# def hello2(request):
#     print ">>>>>>>view"
#     c = RequestContext(request, { })
#     return render_to_response('hello/hello.html', c)