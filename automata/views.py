from django.shortcuts import render
from automata.algo_imp import start_with_a
from automata.algo_imp import even_even
# Create your views here.
data = {}
def home(request):
    if request.method == 'GET':
        btn_val = request.GET.get('input-value')
        btn_algo = request.GET.get('input-algo')
        # START WITH A ALGO PART01
        if(btn_algo == "start_with_a"):
            values, exps = (start_with_a.check_value(btn_val))
            data={
                'value':values,
                'exp':exps
                }
            return render(request, 'show.html',data)

            # even even algo runing
        if(btn_algo == "even_even"):
            values, exps = (even_even.check_value(btn_val))
            data={
                'value':values,
                'exp':exps
                }
            return render(request, 'show.html',data)
    return render(request,'home.html')

def show(request):
    pass
    

