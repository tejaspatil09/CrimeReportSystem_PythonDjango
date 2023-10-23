from django.contrib.auth import authenticate, login
from django.shortcuts import redirect,render
from django .views.generic import  View
from .forms import *
from django.contrib import messages
from .models import AddComplaint
# Create your views here.

def home(request):
    return render(request, 'core/home.html ')

class SignupView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request, 'core/signup.html' , {'form':fm})
    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"SignUp Succesfully")
            return redirect('/signup')
        else:
            return render(request, 'core/signup.html', {'form': fm})

class LoginView(View):
    def get(self,request):
        fm = LoginForm()
        return render(request,'core/login.html',{'form':fm})

    def post(self , request):
        fm = LoginForm(request , data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            user = authenticate(request , username=username ,password = password)
            if user is not  None :
                login(request,user)
                return  redirect('/')
            else:
                return render(request, 'core/login.html', {{'form': fm}})
        else:
            return render(request,'core/login.html', {{ 'form': fm  }})

class Addcomplaint(View):
    def get(self,request):
        fm = AddComplaintForm ()
        return render(request,'core/addcomplaint.html',{'form':fm})

    def post(self, request):
        fm = AddComplaintForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/addcomplaint.html', {'form': fm})

class Viewcomplaint(View):
   def get(self,request):
        user_data = self.request.user
        comp_data = AddComplaint.objects.filter(username=user_data)
        return render(request,'core/viewcomplaint.html',{'compdata':comp_data , 'userdata':user_data})



class AdminloginView(View):
    def get(self,request):
        return render(request,'core/adminlogin.html')