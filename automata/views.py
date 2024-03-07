from django.shortcuts import render

# Create your views here.

def test(request):
    print("hello")
    return render(request,'home.html')