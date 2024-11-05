from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Book
def myappHome(req):
    return render(req,'index.html',{"title":'home','content':'This is home content'})
def about(request):
    page={
        'title':'about',
        'content':'This is about page content'
    }
    return render(request,'about.html',page)
def profile(request):
     social =['facebook:me.facebook.com','github:me.github.com','instagram:me.instagram.com']
     return render(request,'profile.html',{'title':'profile','social':social})
 
#inserting data to database:
def insert_data(request):
    book = Book(
        title="double standard",
        author="shakti",
        publish_date="2005-03-11",
        isbn_number="849474847484789"
    )
    
    book.save()
    return HttpResponse("Data inserted successfully")

def display_books(request):
    books = Book.objects.all().values()
    print(books)
    return render(request,"allBooks.html",context={"allBooks":books})
