from django.contrib.auth.models import AbstractUser
from django.db import models


class BetterUser(AbstractUser):
    CHOICES = (
        ('RANDOM', 'Random'),
        ('YOURCHOICE', 'Yourchoice'),
    )
    STATE = (
        ('AL', 'AL'),
        ('AK', 'AK'),
        ('AZ', 'AZ'),
        ('AR', 'AR'),
        ('CA', 'CA'),
        ('CO', 'CO'),
        ('CT', 'CT'),
        ('DE', 'DE'),
        ('FL', 'FL'),
        ('GA', 'GA'),
        ('HI', 'HI'),
        ('ID', 'ID'),
        ('IL', 'IL'),
        ('IN', 'IN'),
        ('IA', 'IA'),
        ('KS', 'KS'),
        ('KY', 'KY'),
        ('LA', 'LA'),
        ('ME', 'ME'),
        ('MD', 'MD'),
        ('MA', 'MA'),
        ('MI', 'MI'),
        ('MN', 'MN'),
        ('MS', 'MS'),
        ('MO', 'MO'),
        ('MT', 'MT'),
        ('NE', 'NE'),
        ('NV', 'NV'),
        ('NH', 'NH'),
        ('NJ', 'NJ'),
        ('NM', 'NM'),
        ('NY', 'NY'),
        ('NC', 'NC'),
        ('ND', 'ND'),
        ('OH', 'OH'),
        ('OK', 'OK'),
        ('OR', 'OR'),
        ('PA', 'PA'),
        ('RI', 'RI'),
        ('SC', 'SC'),
        ('SD', 'SD'),
        ('TN', 'TN'),
        ('TX', 'TX'),
        ('UT', 'UT'),
        ('VT', 'VT'),
        ('VA', 'VA'),
        ('WA', 'WA'),
        ('WV', 'WV'),
        ('WI', 'WI'),
        ('WY', 'WY')
    )
    choice = models.CharField(max_length=10,
                                      choices=CHOICES,
                                      default='YOURCHOICE')
    state = models.CharField(max_length=10,
                                      choices=STATE,
                                      default='AL')
    city = models.CharField(max_length=25)

    def __unicode__(self):
        return u"{}".format(self.username)


class RainFavourite(models.Model):
    user = models.ForeignKey(BetterUser, related_name='use')
    choice = models.CharField(max_length=160)

    def __unicode__(self):
        return u"{}".format(self.user)


class SunFavourite(models.Model):
    user = models.ForeignKey(BetterUser, related_name='user')
    choice = models.CharField(max_length=160)

    def __unicode__(self):
        return u"{}".format(self.user)


class SnowFavourite(models.Model):
    user = models.ForeignKey(BetterUser, related_name='users')
    choice = models.CharField(max_length=160)

    def __unicode__(self):
        return u"{}".format(self.user)