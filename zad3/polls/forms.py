from django import forms

from .models import Enrollment, Courses

class NewCourse(forms.ModelForm):
    
    class Meta:
        model = Courses
        fields = ('name','amount_of_places','date')

