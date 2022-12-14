from django.http import HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print("process view")
        # return HttpResponse("this is before view")
        return None
    
class my_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time initilization")

    def __call__(self,request):
        print("this is before view")
        response=self.get_response(request)
        print("after view")
        return response

class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print("exception occured")
        class_name = exception.__class__.__name__
        print("class name == ",class_name)
        msg = exception
        print("raised exception == ",msg)
        return HttpResponse(msg)
