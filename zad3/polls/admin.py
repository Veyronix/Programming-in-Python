from django.contrib import admin

from .models import Question, People, Courses,Enrollment

admin.site.register(Question)
admin.site.register(People)
admin.site.register(Courses)
admin.site.register(Enrollment)
