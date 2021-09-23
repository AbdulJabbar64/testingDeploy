from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class  testing:
    def index(request):
        return HttpResponse("<h1>hello world</h1>")