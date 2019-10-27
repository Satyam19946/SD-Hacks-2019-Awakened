from django.contrib import admin

# Register your models here.
from .models import Driver

admin.site.site_header = "Awakened Admin"
admin.site.site_title = "Awakened Admin Area"
admin.site.index_title = "Welcome to Awakened Area"
admin.site.register(Driver)