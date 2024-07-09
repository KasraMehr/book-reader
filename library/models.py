from django.db import models


class Book(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
