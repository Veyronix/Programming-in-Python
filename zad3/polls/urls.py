from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/5/TO
    path('<int:course_id>/name', views.course_detail, name='name'),
    # ex: /polls/
    path('', views.courses, name='courses'),
    # ex: /polls/new_course
    path('new_course',views.new_course,name = 'new_course'),
    # ex: /polls/Ruby/new_enrollment
    path('<str:name>/new_enrollment',views.new_enrollment,name = 'new_enrollment')
    
]
