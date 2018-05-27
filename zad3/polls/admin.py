from django.contrib import admin

from .models import People, Courses,Enrollment

admin.site.register(People)
admin.site.register(Courses)
admin.site.register(Enrollment)
