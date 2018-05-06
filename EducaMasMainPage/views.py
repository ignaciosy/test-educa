import os

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .forms import ContactForm, BlogForm
from .models import Blog

from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about-us.html')


def alumnos(request):
    return render(request, 'alumnos.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def postulaciones(request):
    return render(request, 'postulaciones.html')


def voluntarios(request):
    return render(request, 'voluntarios.html')


def blog(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }
    return render(request, 'blog.html', context)


def blog_upload(request):
    return render(request, 'blog_upload.html')


def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                print(subject+from_email+message)
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact-us.html", {'form': form})

def blog_upload(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()
    context = {
        "blog_form": form
    }
    return render(request, 'blog_upload.html', context)

def delete_blog(request):
    checks = request.POST["checks_form"]
    checks = checks.split(',')

    for i in range(len(checks)):
        #if pics_check[i] != '':
        blog = Blog.objects.get(id_int=checks[i])
            
        path = settings.MEDIA_ROOT + "/" + str(blog.Foto)
        print (path)
        if os.path.isfile(path):
            os.remove(path)
        blog.delete()
        
    return redirect('blog')

