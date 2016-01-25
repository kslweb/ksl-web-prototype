from django.contrib import admin
from .models import Post, AboutUs, ContactUs

admin.site.register(Post)
admin.site.register(AboutUs)
admin.site.register(ContactUs)