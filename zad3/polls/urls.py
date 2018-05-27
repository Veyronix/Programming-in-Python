from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/course
    # path('<int:course_id>/course', views.course_detail, name='course_detail'),
    path('<int:course_id>/name', views.course_name, name='name'),
    # ex: /polls/courses
    path('courses', views.courses, name='courses'),
    
    path('<str:name>/add_course',views.add_course,name = 'add_course'),

    path('new_course',views.new_course,name = 'new_course'),

    path('<str:name>/new_enrollment',views.new_enrollment,name = 'new_enrollment')

    # path('signed_up',views.new_enrollment,name = 'new_enrollment')

]
