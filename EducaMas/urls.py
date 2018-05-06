"""EducaMas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from EducaMasMainPage import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^about_us/', TemplateView.as_view(template_name="about-us.html"), name='about_us'),
    url(r'^voluntarios/', TemplateView.as_view(template_name="voluntarios.html"), name='voluntarios'),
    url(r'^alumnos/', TemplateView.as_view(template_name="alumnos.html"), name='alumnos'),
    url(r'^postulaciones/', TemplateView.as_view(template_name="postulaciones.html"), name='postulaciones'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^blog_upload/', views.blog_upload, name='blog_upload'),
    url(r'^delete_blog/', views.delete_blog, name='delete_blog'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
