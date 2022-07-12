from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    post_date=models.DateField()
    details=models.TextField()