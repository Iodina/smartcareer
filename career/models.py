from django.db import models

# Create your models here.

class Profession(models.Model):
    sphere = models.ManyToManyField('Sphere')
    skill = models.ManyToManyField('Skill')
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Sphere(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    sphere = models.ForeignKey('Sphere')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name







