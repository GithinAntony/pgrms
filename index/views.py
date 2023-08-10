from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'index/home.html')

def about(request):
    return render(request, 'index/about.html')

def contact_us(request):
    return render(request, 'index/contact.html')

def feature(request):
    return render(request, 'index/feature.html')

def team(request):
    return render(request, 'index/team.html')
