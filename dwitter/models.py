from django.db import models

# Create your models here.
# dwitter/models.py

from django.db import models
#import the built-in User model that you want to extend.
from django.contrib.auth.models import User


class Profile(models.Model):
    # a OneToOneField object called user, representing the profile’s connection to the
    #  user that was created with Django’s
    #  built-in user management app.
    #  define that any profile will get deleted if the associated user gets deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #  define a ManyToManyField object with the field name follows, which can hold connections to other user profiles.
    follows = models.ManyToManyField(
        "self",
        #  the related_name argument allows you to access the profiles that follow a specific profile.
        related_name="followed_by",
        #  symmetrical=False means that if profile A follows profile B, it does not imply that profile B follows profile A.
        symmetrical=False,
        #  blank=True allows the field to be empty, meaning a profile can exist without following any other profiles.
        blank=True
    )