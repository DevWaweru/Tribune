from django.test import TestCase
from .models import Article, Tag
import datetime as dt
# Create your tests here.
# class EditorTestClass(TestCase):

#     # Set up method
#     def setUp(self):
#         self.richard= Editor(first_name = 'Richard', last_name ='Waweru', email ='example@abc.com')
    
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.richard,Editor))
    
#     # Testing Save Method
#     def test_save_method(self):
#         self.richard.save_editor()
#         editors = Editor.objects.all()
#         self.assertTrue(len(editors) > 0)
    
class ArticleTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.richard = Editor(first_name='Richard', last_name='Waweru', email = 'example@abc.com')
        self.richard.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tag(name='testing')
        self.new_tag.save()

        self.new_article = Article(title='Test Article', post = 'This is a random test post', editor=self.richard)
        self.new_article.save()
        
        self.new_article.tags.add(self.new_tag)
    
    def tearDown(self):
        Editor.objects.all().delete()
        Tag.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)
