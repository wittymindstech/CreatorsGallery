# Create your views here.

from django.shortcuts import render, redirect
from wtpixel.forms import ImageForm
from django.contrib import messages
from wtpixel.models import Image

def index(request):
    portfolio = Image.objects.all()
    context = {"portfolio": portfolio}
    return render(request, "index.html", context)

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image inserted successfully.')
            return redirect('upload')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})



