from django.contrib import admin
from . models import Car, Comment, Website


# Register your models here.
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Website)