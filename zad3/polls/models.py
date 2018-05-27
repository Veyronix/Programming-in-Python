from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length = 200)
    amount_of_places = models.IntegerField(default = 0)
    date = models.DateTimeField('date of term')
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length = 25)
    surname = models.CharField(max_length = 40)
    def __str__(self):
        return self.name +" "+ self.surname

class Enrollment(models.Model):
    course = models.ForeignKey(Courses,on_delete = models.CASCADE)
    person = models.ForeignKey(People,on_delete = models.CASCADE)

    


