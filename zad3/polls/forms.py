from django import forms

from .models import Courses, People

class NewCourse(forms.ModelForm):
    
    class Meta:
        model = Courses
        fields = ('name','amount_of_places','date')

class NewEnrollment(forms.ModelForm):

    class Meta:
        model = People
        fields = ('name','surname')

