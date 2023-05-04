from django.shortcuts import render


# Create your views here.
def index(request): return render(request, 'index.html', {'utxos': {'uxtos': 'Are Over 9000!'}})

def next(request): return render(request, 'next-page.html')

def prev(request): return render(request, 'prev-page.html')