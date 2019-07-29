from django.shortcuts import render

# Create your views here.
def privatepage(request):
    return render(request, 'privatepage.html')