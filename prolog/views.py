from django.shortcuts import render

# Create your views here.
def prolog(request):
    return render(request, 'prolog.html')