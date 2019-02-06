from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#added view for this
def index(request):
    """
    The root view of my app.

    :param request:
    :return:
    """
    return render(request, 'contacts/index.html')

