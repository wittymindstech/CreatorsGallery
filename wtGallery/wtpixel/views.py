# Create your views here.

# from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.conf import settings
# from django.core.files.storage import FileSystemStorage
from wtpixel.forms import ImageForm
from django.contrib import messages

def index(request):
    return render(request, "index.html")

# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#         messages.success(request, 'Image inserted successfully.')
#     return render(request, 'upload.html', context)

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