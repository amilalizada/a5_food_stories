from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class CustomMiddleware(MiddlewareMixin):
    white_list = [
        '172.30.95.48'
    ]
    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))
        if request.META.get('REMOTE_ADDR') not in self.white_list:
            return HttpResponse('You are not allowed')
        
        return None