from django.shortcuts import render


def index(request):
    return render(request, 'homePage.html')


def contact(request):
    return render(request, 'basic.html', {'values': ['Any questions???'
                                                     ' call 911 they will help, or pUGShOLE123@GMAIL.COM ']})
