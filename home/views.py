from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from design.models import DesignFeed
# Create your views here.

def NoneTag(request):
    return redirect("/home/None/")

def home(request, previousTag):
    reccentTag = previousTag
    pieces = DesignFeed.objects
    return render(request,'home.html',{'pieces':pieces, 'reccentTag':reccentTag})

def new(request):
    return render(request,'new.html')

def create(request):
    piece = DesignFeed()
    piece.title = request.GET['title']
    piece.description = request.GET['body']   
    piece.pub_date = timezone.datetime.now()
    piece.image = request.GET['image']
    piece.save()
    return redirect('/home/detail/' + str(piece.id))

def detail(request, image_id):
    image_detail = get_object_or_404(DesignFeed, pk= image_id)
    return render(request, 'detail.html', {'images': image_detail})