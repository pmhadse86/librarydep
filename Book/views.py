from django.db.models.fields import DateField
from .models import Book
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import date
from django.core.mail import send_mail
from django.conf  import settings
# Create your views here.

def homepage(request):
    if request.method == "POST":
        data = request.POST
        if not data.get("id"):
            if data.get("ispub") == "Yes":
                obj = Book.objects.create(name = data["nm"],
                qty = data["qty"], 
                price = data["price"], 
                is_published = True,
                published_date=date.today())
            elif data.get("ispub") == "No":
                obj = Book.objects.create(name = data["nm"],
                    qty = data["qty"], 
                    price = data.get("price"))
            sub1= "Book Entry"
            msg =f"Book Name : {data['nm']} created successfully"
            send_mail(subject= sub1, message= msg, from_email=settings.EMAIL_HOST_USER, recipient_list=["pmhadse.86@gmail.com"])
            return redirect("home")
        else:
            bid =  data.get("id")
            book = Book.objects.get(id = bid)
            book.name = data["nm"]                    
            book.qty = data["qty"]                    
            book.price = data["price"]           
            if  data["ispub"] == "Yes" :
                if book.is_published:
                    pass
                else:
                    book.is_published = True
                    book.published_date=date.today()
            elif data["ispub"] == "No" :
                if book.is_published ==True:
                        pass
                else:
                    book.is_published = False
            book.save()
            
            return redirect("home")

    else:
        return render(request, template_name="home.html")

def get_books(request):
    books = Book.objects.all()
    return render(request, template_name="books.html", context={"all_books": books})

def delete_book(request, id):
    obj = Book.objects.get(id=id).delete()
    sub1= "Book Delete"
    msg = f"Book  id:{id} deleted"
    send_mail(subject= sub1, message= msg, from_email=settings.EMAIL_HOST_USER, recipient_list=["pmhadse.86@gmail.com"])
    return redirect("show-book")

def update_book(request, id):
    book = Book.objects.get(id=id)
    sub1= "Book Update"
    msg = f"Book id:{id} updated successfully"
    send_mail(subject= sub1, message= msg, from_email=settings.EMAIL_HOST_USER, recipient_list=["pmhadse.86@gmail.com"])
    return render(request, template_name="home.html", context={"edit_book": book})

def  soft_delete(request, id):
    book = Book.objects.get(id= id)
    book.is_deleted = "Y"
    book.save()
    sub1= "Book Soft-Delete"
    msg = f"Book with id {id} soft- deleted"
    send_mail(subject= sub1, message= msg, from_email=settings.EMAIL_HOST_USER, recipient_list=["pmhadse.86@gmail.com"])
    return redirect("show-book")

def active_books(request):
    act_books = Book.objects.filter(is_deleted = "N")
    return render(request, "books.html", {"all_books": act_books})

def in_active_books(request):
    inact_books = Book.objects.filter(is_deleted = "Y")
    return render(request, "books.html", {"all_books": inact_books, "book_status": "InActive"})

def  restore_books(request, id):
    res_book = Book.objects.get(id = id)
    res_book.is_deleted = "N"
    res_book.save()
    sub1= "Book Restore"
    msg = f"Book with id {id} restored"
    send_mail(subject= sub1, message= msg, from_email=settings.EMAIL_HOST_USER, recipient_list=["pmhadse.86@gmail.com"])
    return redirect("show-book")



