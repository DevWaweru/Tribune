from django.db import models
# from tinymce import models as tinymce_models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime as dt

# # Create your models here.
# class Editor(models.Model):
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=30, blank=True)

#     def __str__(self):
#         return self.first_name
    
#     def save_editor(self):
#         self.save()

#     class Meta:
#         ordering=['first_name']
    
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=30)
    post = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', default='Image')

    @classmethod
    def today_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
class NewsLetterRecepients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()