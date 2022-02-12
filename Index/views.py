from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # aboutdata=about.objects.all()[0]
    # sliderdata=slider.objects.all()
    # clientsdata=clients.objects.all()
    # portfoliodata=portfolio.objects.all()
    #
    # diction={'about':aboutdata, 'slider':sliderdata,'clients':clientsdata, 'portfolio':portfoliodata}
    return render(request,'index.html')

def blog1(request):
    return render(request,'blog1.html')

def blog2(request):
    return render(request,'blog2.html')

def blog3(request):
    return render(request,'blog3.html')
