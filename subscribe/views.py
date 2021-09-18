from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import Subscribe
from django.core.mail import send_mail, EmailMessage

from django.conf  import settings

# Create your views here.

# s = Subscribe()
# print(s)

def subscribe_mail(request):
        sub = Subscribe()                               # Subscribe class/ form
        # print(sub)                              
        # return HttpResponse("hi")
        if  request.method == "POST":
                sub = Subscribe(request.POST)
                sub1 = "Welcome to Django Email system"
                msg1 = "Enjoy Django programming"
                recipient  = request.POST["Email"].strip()
                if  ";"  in recipient:
                        rec_list = recipient.split(";")
                else:
                        rec_list = [recipient]
                ## send simple  mail
                # send_mail(subject= sub1, message= msg1, from_email=settings.EMAIL_HOST_USER, recipient_list= rec_list)
                ## send mail with attachment                        
                msg = EmailMessage(subject=sub1, body=msg1, from_email=settings.EMAIL_HOST_USER, to=rec_list)
                msg.attach_file(path = "C:\\Users\\Prabhakar\\Desktop\\Test_mail _file.txt")
                msg.send(fail_silently = True)
                
                return render(request, 'success.html',{"recipient" : rec_list})
        return render(request, 'index.html', {'form1': sub})

