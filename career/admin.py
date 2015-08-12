from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models
# Register your models here.
from career.models import *



class ProfessionAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'10'})}, }
    list_display = ('name', 'sphere')



class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','sphere', 'link')

admin.site.register(Sphere)
admin.site.register(Skill)
admin.site.register(Course, CourseAdmin)

admin.site.register(Profession, ProfessionAdmin)

