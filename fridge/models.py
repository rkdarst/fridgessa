from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class FUser(models.Model):
    user = models.OneToOneField(User)


class Location(models.Model):
    name = models.CharField(max_length=64)
    users = models.ManyToManyField(User)
    def __unicode__(self):
        return u"Location(%s)"%self.name

class Item(models.Model):
    loc = models.ForeignKey('Location')

    ctime = models.DateTimeField("time bought", auto_now_add=True)
    etime = models.DateTimeField("time expires", null=True)
    product = models.ForeignKey('Product')

    shelf = models.ForeignKey('Shelf')
    def __unicode__(self):
        return u"Item(%s, %s)"%(self.pk, self.product.name)



class Product(models.Model):
    name = models.CharField(max_length=64)
    lifetime = models.IntegerField('expiry days')
    loc = models.ForeignKey('Location')
    def __unicode__(self):
        return u"Product(%s)"%self.name

class Shelf(models.Model):
    name = models.CharField(max_length=64)
    loc = models.ForeignKey('Location')
    def __unicode__(self):
        return u"Shelf(%s)"%self.name
