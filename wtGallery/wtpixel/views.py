# Create your views here.
from django import template
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import ListView
from wtpixel.forms import ImageForm, SignUpForm, LoginForm
from django.contrib import messages
from wtpixel.models import Image

@login_required(login_url="/login/")
def index(request):
    portfolio = Image.objects.all()
    context = {"portfolio": portfolio}
    return render(request, "index.html", context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = "Username or Password Doesn't match"
        else:
            msg = 'Error validating the form'
    return render(request, "login.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
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

class SearchResultsView(ListView):
    model = Image
    template_name = 'search_results.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Image.objects.filter(Q(title__icontains=query) | Q(image__icontains=query))
        return object_list

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))