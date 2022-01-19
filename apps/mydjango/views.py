from django.shortcuts import render

# Create your views here.

def goIndex(request):
    return render(request, 'goIndex.html')