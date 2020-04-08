from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# this signal gets fired when an object is saved
# we will need to import User model when a user is created and the user model will be the sender since it will be the one which will send the signal
# we will need to import a receiver which will be a function that gets this signal and be able to perform some task
# lastly we will need to import profile since we will be creating a profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
#         we have a create profile function that we want to run every time a user is created , we are going to use the receiver we imported and use it as a decorator and it will take arguments such as post_save and sender=User
#  we have a sender which is the user , and the signal of post_save , this says that when a user is saved then send this signal and the signal is going to be received by the receiver decorator(the receiver is the create profile function which takes arguments such as sender , instance , created which our post_save signal passed to it   )
# we say if the user was created  then create a profile object with the user = the instance of the user that was created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#     kwargs accepts any additional keyword arguments

