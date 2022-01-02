from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import image
from .forms import createForm
# Create your views here.
def home_view(request):
    return render(request,'home.html',{})
def images_view(request):
    images = image.objects.all()
    return render(request,'gallery.html',{"images":images})
def detail_view(request,id):
    imageObj = image.objects.get(id = id)
    return render(request,'detail.html', {"image":imageObj})
def create_view(request):
    form = createForm()
    return render(request,'create.html',{"form":form})
def submitForm_views(request):
    form = createForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return render(request,'created.html',{})
def delete_view(request,id):
    imageObj = image.objects.get(id = id)
    imageObj.delete()
    return HttpResponseRedirect("/images")