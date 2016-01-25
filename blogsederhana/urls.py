"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Post, AboutUs
from . import views

urlpatterns = [
	#url(r'^$', ListView.as_view(
			#queryset = Post.objects.all().order_by('-created'),
			#template_name = 'blog.html'
		#)),
	
	url(r'^$', 'blogsederhana.views.listing'),
	url(r'^(\d+)', 'blogsederhana.views.detail_artikel'),
	url(r'^aboutus/', 'blogsederhana.views.about_us'),
	url(r'^contactus/', 'blogsederhana.views.contact_us'),
	url(r'^tag/(?P<tag>\w+)', 'blogsederhana.views.tagpage'),
	url(r'^search/$', 'blogsederhana.views.search'),
]