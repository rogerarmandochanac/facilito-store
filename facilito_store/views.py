from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
    user = authenticate(username=username, password=password)
    
    if user:
        login(request, user)
    
    return render(request, "users/login.html", {})