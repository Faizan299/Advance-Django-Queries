from ast import alias
from unicodedata import name
from django.shortcuts import render
from django.db.models.functions import Cast,Coalesce,Greatest,JSONObject, Lower
from django.db.models import FloatField,Sum,DateTimeField,F
from django.utils import timezone
import author
from .models import Author_1,Author, Blog,Coment
# Create your views here.



def abc(request):
    Author_1.objects.create(name='Ali',age=30)
    author = Author_1.objects.annotate(age_as_float=Cast('age', output_field=FloatField()),).values('age_as_float')
    context={'auth':author}
    return render(request,'cast.html',context)

def xyz(request):
    Author_1.objects.create(name='Faizan',goes_by='Maggie')
    aggregated = Author.objects.aggregate(combined_age=Sum('age'),combined_age_default=Sum('age', default=0),combined_age_coalesce=Coalesce(Sum('age'), 0))
    now = timezone.now()
    Coalesce('updated', Cast(now, DateTimeField()))
    con={'au':aggregated}
    return render(request,'cast.html',con)

# def xyz(request):
#     Author_1.objects.create(name='Faizan',goes_by='Maggie')
#     author1=Author_1.objects.annotate(screen_name=Coalesce('name','alias','goes_by'))
#     cont={'aut':author1}
#     return render(request,'cast.html',cont)

def great(request):
    blog=Blog.objects.create(body='Greatest is the best.')
    comment = Coment.objects.create(body='No, Least is better.', blog=blog)
    comments = Coment.objects.annotate(last_updated=Greatest('modified', 'blog__modified')).values('last_updated')
    conta={'com':comments}
    return render(request,'cast.html',conta)

def jso(request):
    Author.objects.create(name='Marget Smith',alias='misth',age=25)
    author=Author.objects.annotate(json_object=JSONObject(
        name=Lower('name'),
        alias='alias',
        age=F('age') * 2,
    )).values('json_object')
    
    # conte={'js':author}
    return(request,'cast.html')
    


    



