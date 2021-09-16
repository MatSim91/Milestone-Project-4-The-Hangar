from django.shortcuts import render

# Create your views here.

def index(request):
    """ View that retuns index page """
    
    return render(request, 'home/index.html')