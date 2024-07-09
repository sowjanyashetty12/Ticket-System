from django.shortcuts import render,redirect
from . forms import registeration,LoginForm ,CreateRecordForm,UpdateRecordForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from . models import Tickets
# Create your views here.
def index(request):
    return render(request,'index.html')
def registeruser(request):
    if request.method=="POST":
        form=registeration(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'loginpage.html')
        else:
            messages.error(request,"Invalid username or password")
            return redirect("register")

    elif request.method=="GET":
        form=registeration()
        return render(request,'register.html',{'form':form})
def loginuser(request):
    if request.method=="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                # if user exists then login logic
                auth.login(request,user)
                return redirect("dashboard")
            else:
                messages.warning(request,"You need to create your account first")
                return redirect("register")


    elif request.method=="GET":
        form=LoginForm()
        return render(request,"loginpage.html",{'form':form})

def userlogout(request):
    auth.logout(request)
    return redirect("index")
    

@login_required(login_url="login")
def dashboard(request):
    my_records=Tickets.objects.all()
    context={'records':my_records}
    return render(request,"dashboard.html",context)

@login_required(login_url="login")
def create_record(request):
    if request.method=="GET":
        form=CreateRecordForm()
        return render(request,"createticket.html",{"form":form})
    if request.method=="POST":
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")


@login_required(login_url="login")
def update_record(request,pk):
    record=Tickets.objects.get(id=pk)
    #below will prefill the form
    form=UpdateRecordForm(instance=record)
    if request.method=='POST':
         form=UpdateRecordForm(request.POST,instance=record)   #this will take the instance from the form and post
         if form.is_valid():
            form.save()
            messages.success(request,"Ticket has been updated")
            return redirect("dashboard")
    
    else:  
     return render(request,"updaterecord.html",{'form':form})

@login_required(login_url="login")
def viewrecord(request,pk):
    record=Tickets.objects.get(id=pk)
    return render(request,"viewrecord.html",{'record':record})

@login_required(login_url="login")
def deleterecord(request,pk):
    record=Tickets.objects.get(id=pk)
    record.delete()
    messages.success(request,"Ticket has been deleted successfully")
    return redirect("dashboard")
   