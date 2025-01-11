from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index_view(request):
    return render(request, "index.html", {})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(username=username, password=password)
    
        if user:
            login(request, user)
            messages.success(request, "Usuario logeado exitosamente")
            return redirect("index")
        else:
            messages.error(request, "El usuario no se encuentra registrado")
    
    return render(request, "users/login.html", {})

def logout_view(request):
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente")
    return redirect("login")