from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=False)


class Student(User):

    def save(self, *args, **kwargs):
        self.is_staff = False
        # self.groups.clear()
        # self.groups.add(Group.objects.filter(name='std').first())
        return super(Student, self).save(*args, **kwargs)

    class Meta:
        proxy = True


class Admin(User):
    def save(self, *args, **kwargs):
        self.is_staff = True
        # self.groups.clear()
        # self.groups.add(Group.objects.filter(name='admin').first())
        return super(Admin, self).save(*args, **kwargs)

    class Meta:
        proxy = True


class Course(models.Model):
    course_name = models.TextField(max_length=255)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self) -> str:
        return self.course_name
