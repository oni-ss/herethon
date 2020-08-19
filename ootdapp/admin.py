from django.contrib import admin
 
# Register your models here.
from ootdapp.models import Write
from .models import Content

admin.site.register(Write)
admin.site.register(Content)