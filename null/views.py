from django.shortcuts import render

# Create your views here.
def dashbord(request):
    return render(request,'index.html')
def staticnavigation(request):
    return render(request,'charts.html')
def table(request):
    return render(request,"table.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def password(request):
    return render(request,"password.html")
def four(request):
    return render(request,"401.html")
def five(request):
    return render(request,"404.html")
def hundre(request):
    return render(request,"500.html")
def layout(request):
    return render(request,"layout.htmnl")
def layout2(request):
    return render(request,"lalyou-static.html")