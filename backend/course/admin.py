from django.contrib import admin
from .models import Course, Student, Admin

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Admin)
