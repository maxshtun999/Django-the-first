from django.db import models

# Create your models here.

class Help(models.Model):

    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length=20)
    e_mail = models.EmailField(default="example@example.com")
    text = models.TextField(default=" ")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


