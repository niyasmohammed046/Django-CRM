from django.shortcuts import render,redirect
from django .contrib.auth import authenticate,login,logout
from django.contrib import messages

def homepage(request):
    #check to see user if login in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In")
            return redirect('homepage')
        
        else:
            messages.success(request,'There was a error loggin in,Please try Again...')
            return redirect('homepage')
        
    else:
        return render(request,'homepage.html',{})
    


def logout_user(request):
    logout(request)
    messages.success(request,'You are logged Out..')
    return redirect('homepage')

def register_user(request):
    return render(request,'register.html',{})