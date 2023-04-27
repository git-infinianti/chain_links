from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def next_page(request):
    return render(request, 'next-page.html')

def prev_page(request):
    return render(request, 'prev-page.html')