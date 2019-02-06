from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import HelpForm
from news.models import News


# Create your views here.
# added view for this
# def index(request):
#     return render(request, 'Help/index.html')

def index(request):

    if request.method == "POST":
        form = HelpForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            return redirect('/help/thanks')

    else:
        form = HelpForm()

    return render(request, 'Help/index.html', {'form' : form})

def thanks(request):

    return render(request, 'Help/thanks.html')

