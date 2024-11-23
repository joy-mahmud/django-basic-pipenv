from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Author,Book,Profile
from .forms import ProfileForm
from django.forms.models import model_to_dict
# Create your views here.
def home(request):
    authors=Author.objects.all()
    context={
        "authors":authors
    }
    
    return render(request,'home.html',context)

def addProfile(request,id):
    #author= Author.objects.get(id=id)
    author = get_object_or_404(Author, id=id)
    
    if request.method=="POST":
        profileForm=ProfileForm(request.POST)
        if profileForm.is_valid():
            profile =profileForm.save(commit=False)
            # profile.author=author
            profile.save()
            return redirect('library_home')
    
    form=ProfileForm(instance=author)
    context={
        "form":form
    } 
    return render(request,'addProfile.html',context=context)  
    
   

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
            #books=author.books.all()
            books=Book.objects.filter(author_id=author.id)        
            booksOfAnAuthor=[]
            for book in books:
                book_data={
                    'title':book.title,
                    'published':book.published_date
                }
                booksOfAnAuthor.append(book_data)
                # book_dict=model_to_dict(book)
                # booksOfAnAuthor.append(book_dict)
            
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
    
    #return testingTwo()
    
    def testingThree():
        author1 = Author.objects.get(id=1)
        author2 = Author.objects.get(id=2)

        # Assuming 'authors' is a ManyToManyField in the Book model
        book = Book.objects.get(id=1)
        book.authors.add(author1, author2)

        # Get all authors of the book
        authors = []
        for author in book.authors.all():
            authors.append(
                {
                    "name": author.name,
                    "website": author.profile.website if hasattr(author, 'profile') else None,
                    "bio": author.profile.bio if hasattr(author, 'profile') else None,
                }
            )

        # Get all books of an author
        # books = []
        # for book in author1.books.all():
        #     books.append({
        #         "title": book.title,
        #         "published": book.published_date
        #     })
        books=[{"title":book.title,"published":book.published_date} for book in author1.books.all()]
        

        return JsonResponse({"authors": authors, "books": books})
    return testingThree()

    
    
    def testProfile():
        author=Author.objects.create(name="Author Four",email='author4@gmail.com')
        profile =Profile.objects.create(
            author=author,
            bio="Author Four has written many bestsellers.",
            website="https://authorfour.com",
            birthDate='1998-01-15'
        )
        return HttpResponse('profile created for the auhtor Four')
   # return testProfile()
    #return HttpResponse('testing two')
    
    
    
