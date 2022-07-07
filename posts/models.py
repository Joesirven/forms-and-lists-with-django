from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
