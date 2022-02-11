from telnetlib import AUTHENTICATION
from tokenize import Comment
from django.contrib import admin
from .models import Author, Author_1,Blog,Coment
# Register your models here.
admin.site.register(Author)
admin.site.register(Author_1)
admin.site.register(Blog)
admin.site.register(Coment)