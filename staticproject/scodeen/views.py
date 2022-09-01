from django.shortcuts import render

# Create your views here.
def show(request):
    d={'name':'python'}
    return render(request,'scodeen/courses.html',context=d)