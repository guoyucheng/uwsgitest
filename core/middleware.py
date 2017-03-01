# -*- coding: utf-8 -*-


#方法一：装饰器方法 基于方法
def test1(get_response):

    def middleware(request):
        print ">>>>>>>>1"
        response = get_response(request)
        print ">>>>>>>>3"
        return response

    return middleware    

#方法二：装饰器方法 基于对象
class Test2(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print ">>>>>>>>>2"
        response = self.get_response(request)
        print ">>>>>>>>>3"
        return response

#方法三 基于请求/响应中间件模式  这种方式需要在 setting中的MIDDLEWARE_CLASSES增加Test3 相当于激活中间件   常用模式上面两种很少用
class Test3(object):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print ">>>>>>>>in Test3 process_view"

    def process_request(self, request):
        print ">>>>>>>>in Test3 process_requset"
        return None

    def process_response(self, request, response):
        print ">>>>>>>>in Test3 process_response"
        return response

    def process_exception(self, request, exception):
        print ">>>>>>>>in Test3 process_exception"

    def process_template_response(self, request, response):
        print ">>>>>>>>in Test3 process_template_response"
        return response

class Test4(object):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print ">>>>>>>>in Test4 process_view"

    def process_request(self, request):
        print ">>>>>>>>in Test4 process_requset"
        return None

    def process_response(self, request, response):
        print ">>>>>>>>in Test4 process_response"
        return response

    def process_exception(self, request, exception):
        print ">>>>>>>>in Test4 process_exception"

    def process_template_response(self, request, response):
        print ">>>>>>>>in Test4 process_template_response"
        return response


