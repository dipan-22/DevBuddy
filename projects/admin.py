from django.contrib import admin
from .models import Project,Review,tag
# Register your models here.

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(tag)