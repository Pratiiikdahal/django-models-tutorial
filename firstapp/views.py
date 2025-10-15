from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    context={"name":"Pratik Dahal","age":24}
    return render(request,'firstapp/index.html',context=context)