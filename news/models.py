from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    news_headline = models.CharField(max_length=200)
    news_body = models.CharField(max_length=1000, default=" ")
    news_published = models.DateTimeField('published date')

    def __str__(self):
        output = self.news_headline + " was published " + str(
            self.news_published) + " with text" + self.news_body
        return output
