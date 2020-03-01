from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hw_hello_view(request):
    return HttpResponse('Hi its my test')

