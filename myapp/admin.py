from django.contrib import admin
from .models import Ebook, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Ebook)