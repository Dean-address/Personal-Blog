from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    article_content = models.TextField()
    
    def __str__(self) -> str:
        return self.article_title