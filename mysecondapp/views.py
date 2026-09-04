from django.shortcuts import render

# Create your views here.
def mysecondappdashboard(request):
    return render(request,'index2.html')