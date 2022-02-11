from django.db import models


class Author(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveBigIntegerField(null=True , blank=True)
    alias=models.CharField(max_length=50, null=True, blank=True)
    goes_by=models.CharField(max_length=50, null=True, blank=True)
    
class Author_1(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveBigIntegerField(null=True , blank=True)
    alias=models.CharField(max_length=50, null=True, blank=True)
    goes_by=models.CharField(max_length=50, null=True, blank=True)    
    
class Blog(models.Model):
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)

class Coment(models.Model):
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
