from django.shortcuts import render

# Create your views here.

def test(request):
    if request.method == 'GET':
        btn_val = request.GET.get('input-value')
        print(btn_val)
    return render(request,'home.html')