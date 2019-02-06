from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# added view for this
def index(request):
    return render(request, 'Help/index.html')
