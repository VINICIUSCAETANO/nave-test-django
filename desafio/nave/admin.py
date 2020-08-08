from django.contrib import admin

# Register your models here.

from .models import User, Naver, Project

admin.site.register([User, Naver, Project])