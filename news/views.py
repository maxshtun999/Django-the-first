from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News


# Create your views here.
def main(request):
    latest_news_list = News.objects.order_by('-news_published')
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/main.html', context)


def news_detail(request):
    response = 23
    return HttpResponse(response)
