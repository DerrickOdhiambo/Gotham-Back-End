from django.db import models
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
class Movie(models.Model):
    title=models.CharField(max_length=40)
    overview=models.CharField(max_length=200)
    poster=models.CharField(max_length=150)
    trailer=models.CharField(max_length=200,null=True)
    year=models.IntegerField(null=True)


    def __str__(self):
        return self.title
