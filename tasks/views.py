from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm
#Displaying the books
def book_list(request):
    books= Book.objects.all()
    return render(request,"list.html",{"books":books})
    

#Creating a new book
def book_create(request):
    if request.method =="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "create.html", {"form": form})

#Update a book
def book_update(request,pk):
    book= get_object_or_404(Book,pk=pk)
    if request.method=="POST":
        form=BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "update.html",{"form":form})


#Delete a book

def book_delete(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method =="POST":
        book.delete()
        return redirect("book_list")
    return render(request,"delete.html",{"book":book})
