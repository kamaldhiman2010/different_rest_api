from django.contrib import admin
from .models import BlogModel,Movie,Director,Question,Choice
# Register your models here.

admin.site.register(BlogModel)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Question)
admin.site.register(Choice)
