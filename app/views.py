from django.shortcuts import render,HttpResponse,redirect
from .form import signupform,futsalforms,searchform,BookingForm
from .models import futsal_court,Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    users=User.objects.all()
    futsals=futsal_court.objects.all()
    return render(request,"home.html",{'users': users,'futsals':futsals})
def createfutsal(request):
    if request.method=="POST":
        f1=futsalforms(request.POST)
        if f1.is_valid():
            f_name=f1.cleaned_data["futsal_name"]
            f_phone=f1.cleaned_data["futsal_court_phone"]
            f_address=f1.cleaned_data["futsal_court_address"]
            price=f1.cleaned_data["price_per_hour"]
            
            new_futsal=futsal_court(futsal_name=f_name,futsal_court_phone=f_phone,futsal_court_address=f_address,price_per_hour=price)
            new_futsal.save()
            return HttpResponse("successful")
    else:
        f1=futsalforms()
    return render(request,"createfutsal.html",{'form':f1})
def signup(request):
    if request.method == 'POST':
        # Extract form data
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            phone=form.cleaned_data["user_phone"]
            obj=Profile(user=user,phone=phone)
            obj.save()
            return redirect("home") # Replace 'success.html' with your actual success template
    else:
        form=signupform()
    # Handle GET request or other cases where the method is not POST
    return render(request, 'signup.html',{'form':form})
def login_user(request):
    if request.method=="POST":
        us=request.POST["username"]
        pw=request.POST["password"]
        user=authenticate(request,username=us,password=pw)
        if user:
            login(request,user)
            return redirect('home')
    else:
        return render(request,"login.html") 
    return render(request,"login.html") 
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
