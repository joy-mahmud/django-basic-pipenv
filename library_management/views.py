from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Author,Book

# Create your views here.
def home(request):
    return HttpResponse('library')

def testing(request):
    def testingOne():
        books= Book.objects.all()
        bookList=[]
        for book in books:
            bookList.append(
                {
                    'title':book.title,
                    'published_data':book.published_date,
                    'author':book.author.name
                }
            )
        author_books=[]    
        for author in Author.objects.all():
            books=Book.objects.filter(author_id=author.id)        
            booksOfAnAuthor=[]
            for book in books:
                book_data={
                    'title':book.title,
                    'published':book.published_date
                }
                booksOfAnAuthor.append(book_data)
            
            author_books.append(
                {
                    'author_name':author.name,
                    'books':booksOfAnAuthor
                }
            )
            
        print(author_books)
        
        return JsonResponse({'books':bookList,'authors':author_books})
    #return testingOne()

    def testingTwo():
        author_books=[] 
        for author in Author.objects.all():
            books_of_an_author=[]
            for book in author.books.all():
                books_of_an_author.append(
                    {
                        'title':book.title,
                        'published_date':book.published_date
                    }
                )
            author_books.append(
                {
                    "author_name":author.name,
                    "books":books_of_an_author
                }
            )
        return JsonResponse(author_books,safe=False)
    
    return testingTwo()
    #return HttpResponse('testing two')
    
