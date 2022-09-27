from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sobre2/index2.html')