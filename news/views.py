from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import News

# Create your views here.
def main(request):
    latest_news_list = News.objects.order_by('-news_published')
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/main.html', context)

def news_detail(request, news_id):
    news = get_object_or_404(News, pk= news_id)
    return render(request, 'news/detail.html', {'news': news})