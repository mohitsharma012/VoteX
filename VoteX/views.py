from django.shortcuts import render

def index(request):

    return render(request,"index.html")

def about(request):
    
    return render(request, "about.html" )

def contact(request):
    return render(request,"contact.html")

def signin(request):
    return render(request,"signin.html")

def signup(request):
    return render(request,"signup.html")

def upcoming_election(request):
    return render(request,"upcoming_election.html")

def result(request):
    return render(request,"result.html")

def contact(request):
    return render(request,"contact-us-page.html")

def dashboard(request):
    return render(request,"dashboard.html")
