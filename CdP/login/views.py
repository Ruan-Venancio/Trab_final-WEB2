from django.shortcuts import render

def index(request):
    return render(request, 'login/index.html')

# Create your views here.
