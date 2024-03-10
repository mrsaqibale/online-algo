from django.shortcuts import render
from automata.algo_imp import code1
# Create your views here.

def test(request):
    if request.method == 'GET':
        btn_val = request.GET.get('input-value')
        btn_algo = request.GET.get('input-algo')
        if(btn_algo == "code1"):
            {
            print(code1.fun(btn_val))
        }
    return render(request,'home.html')
    

