from.models import Profile
from django.contrib.auth.models import User


# creating signals

from django.db.models.signals import post_save,post_delete

# decorators
from django.dispatch import receiver

# signal creation

# @reciever(post_save,sender=Profile)
# def profileUpdated(sender,instance,created, **kwargs):
def createProfile(sender,instance,created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user,username=user.username,email=user.email,name=user.first_name)
        

def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    print('Deleting user.....')

# post_save.connect(profileUpdated,sender=Profile)

post_save.connect(createProfile,sender=User)

post_delete.connect(deleteUser,sender=Profile)
