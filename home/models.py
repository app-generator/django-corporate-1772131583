# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer_Profile(models.Model):

    #__Customer_Profile_FIELDS__
    customer_code = models.CharField(max_length=255, null=True, blank=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    customer_leid = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_Profile_FIELDS__END

    class Meta:
        verbose_name        = _("Customer_Profile")
        verbose_name_plural = _("Customer_Profile")


class Irc(models.Model):

    #__Irc_FIELDS__
    customer_code = models.ForeignKey(customer_profile, on_delete=models.CASCADE)
    irc_number = models.CharField(max_length=255, null=True, blank=True)
    irc_issue_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    irc_expiry_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Irc_FIELDS__END

    class Meta:
        verbose_name        = _("Irc")
        verbose_name_plural = _("Irc")


class Bin(models.Model):

    #__Bin_FIELDS__
    customer_code = models.ForeignKey(customer_profile, on_delete=models.CASCADE)
    bin_issue_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    bin_expiry_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Bin_FIELDS__END

    class Meta:
        verbose_name        = _("Bin")
        verbose_name_plural = _("Bin")



#__MODELS__END
