from django.db import models
from django.db.models.signals import post_save #import the post_save signal
# Create your models here.
##dwitter/models.py

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
    def __str__(self):
        return self.user.username
    
    # new function called create_profile that uses created, which post_save provides, to decide whether to create a new Profile instance.
    #  code will only continue if the post-save signal indicates that Django created the user object successfully.
    #  If so, it creates a new Profile instance linked to the user and saves it to the database.
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
            user_profile.follows.set([instance.profile.id])
            user_profile.save()

# Create a Profile for each new user.
    post_save.connect(create_profile, sender=User)