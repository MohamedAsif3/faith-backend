from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
#create signals here
'''create signals: for user that will create a token
when new user is created''' 

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):

#     if created:
#         Token.objectsl.create(user=instance)

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)