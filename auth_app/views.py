from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    if request.method == 'POST':
        auth.logout(request)                                                  # It will logout the user
        return redirect('login')

def login(request):
    if request.method == 'POST':                                             
        username = request.POST['username']                                   # It will get the username from the form
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)   # It will authenticate the user according to registered user
        if user is not None:
            auth.login(request, user)                                         # It will login the user
            return redirect('homepage')
        else:
            return redirect('login')                               # If user is not registered then it will redirect to login page
    else:
        return render(request, 'auth_app/login.html')

def register(request):
    if request.method == 'POST':                                             # It handle the form to post the data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']                                   # It will get the username from the form
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            user = User.objects.create_user(username=username, password=password, 
                   email=email, first_name=first_name, last_name=last_name)         # It will create the user
            user.save();
            return redirect('login')
        else:
            return redirect('register') 
    else:
        return render(request, 'auth_app/register.html')

def index(request):
    return render(request, 'sorting_app/index.html')