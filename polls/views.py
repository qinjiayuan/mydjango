from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from djangoProject.models import CrtExpiredRecord
from djangoProject import models
def helloworld(request):
    return HttpResponse("Hello World!")


def queryClient(request):
    msg = models.OtcDerivativeCounterparty.objects.filter(corporate_name='测试产品关注类')
    for i in msg:
        print(i.__dict__)
    return HttpResponse(msg[0].__dict__)
def index(request):
    return render(request,'index.html')
