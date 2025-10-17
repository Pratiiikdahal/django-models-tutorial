from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import employee
# Create your views here.

def first(request):
    emp_data=employee.objects.all()
    newcontext={'emp_data':emp_data}
    #context={"name":"Pratik Dahal","age":24}
    return render(request,'firstapp/index.html',context=newcontext)