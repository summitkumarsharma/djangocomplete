from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse('This is home page')
     return render(request,"index.html")
def about(request):
   # return HttpResponse('This is About page')
     return render(request,"about.html")

def services(request):
   # return HttpResponse('This is Services page')
      return render(request,"services.html")
def contact(request):
   if request.method=="POST":
      name=request.POST.get("name")
      email=request.POST.get("email")
      
      phone=request.POST.get("phone")
      desc=request.POST.get("desc")
      contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
      contact.save()
      messages.success(request, 'Your Message has been sent!.') 

   # return HttpResponse('This is contact page')    
   return render(request,"contact.html")