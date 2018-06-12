from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Courses, People, Enrollment
from .forms import NewCourse, NewEnrollment
from django.shortcuts import redirect
import datetime


def course(request, course_id):
    list_of_people_registered = Courses.objects.filter(id=course_id)
    template = loader.get_template('polls/course.html')
    context = {
        'list_of_people_registered': list_of_people_registered
    }
    return render(request, 'polls/course.html', context)


def courses(request):
    all_courses = Courses.objects.all
    template = loader.get_template('polls/courses.html')
    context = {
        'all_courses': all_courses
    }
    return render(request, 'polls/courses.html', context)


def course_detail(request, course_id):
    name = Courses.objects.filter(id=course_id)[0]
    template = loader.get_template('polls/course_detail.html')
    list_of_people_registered = Enrollment.objects.filter(course_id=course_id)
    amount_of_vacancies = Courses.objects.get(id=course_id).amount_of_places - Enrollment.objects.filter(
        course_id=course_id).count()
    date = Courses.objects.filter(id=course_id)[0].date
    context = {
        'list_of_people_registered': list_of_people_registered,
        'name': name,
        'amount_of_vacancies': amount_of_vacancies,
        'date': date
    }
    return render(request, 'polls/course_detail.html', context)


def new_course(request):
    if request.method == "POST":
        form = NewCourse(request.POST)
        if form.is_valid():
            try:
                if datetime.datetime.now() > datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d %H:%M"):
                    context = "Too late"
                elif int(request.POST['amount_of_places']) <= 0:
                    context = "Bad amount of places."
                elif Courses.objects.filter(name=request.POST['name']).exists():
                    context = "Course already exists"
                else:
                    Courses.objects.create(name=request.POST['name'], amount_of_places=request.POST['amount_of_places'],
                                           date=request.POST['date'])
                    context = "Created course"

            except ValueError:
                context = "Give time of event."

            return render(request, 'polls/signed_up.html', {'context': context})
    else:
        form = NewCourse()
    return render(request, 'polls/new_course.html', {'form': form})


def new_enrollment(request, name):
    if request.method == "POST":
        form = NewEnrollment(request.POST)
        if form.is_valid():
            course_id = Courses.objects.get(name=name)
            People.objects.create(name=request.POST['name'], surname=request.POST['surname'])
            people_pk = People.objects.filter(name=request.POST['name'], surname=request.POST['surname']).first()
            Enrollment.objects.create(course=course_id, person=people_pk)
            return render(request, 'polls/signed_up.html', {'context': "Signed up"})
    else:
        form = NewEnrollment()
    return render(request, 'polls/new_enrollment.html', {'form': form, 'name': name})
