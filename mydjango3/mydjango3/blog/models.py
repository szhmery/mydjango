from django.db import models

sex_choices = (
    ('f', 'female'),
    ('m', 'male'),
)


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=sex_choices)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name

class FileUser(models.Model):
    username = models.CharField(max_length=30)
    headImg = models.FileField(upload_to='./upload/')

    def __unicode__(self):
        return self.username