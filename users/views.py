from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.

def loginUser(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method=='POST':
        username=request.POST['username'] 
        password=request.POST['password'] 
        print(username,password)

        try:
            user=User.objects.get(username=username)
            print("found")
        except:
            messages.error(request,'Username does not exist')

        user=  authenticate(request,username=username,password=password) 

        if user is not None:
            login(request,user)
            print("logging in")
            return redirect('profiles')
        else:
             messages.error(request,'Username or password is incorrect')       
    
    return render(request,'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'User successfully logged out')
    return redirect('login')

def registerUser(request):
    page='register'
    # form=UserCreationForm()
    form=CustomUserCreationForm()

    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User account was created!')

            login(request,user)
            return redirect('profiles')
        
        else:
            messages.success(request,'Error occured during registration')



    context = {'page':page,'form':form}
    return render(request,'users/login_register.html',context)


def profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context={'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)