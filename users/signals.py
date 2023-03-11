from django.contrib.auth.models import User  # using this to copy the attributes into the profile
from django.db.models.signals import post_save, post_delete
from .models import Profile


# sender - model that sends the signal
# instance - model that triggers the signal call
# created (boolean) - notifies if a new record was created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance  # instance is the sender from the post_save
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def profile_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_delete.connect(profile_delete, sender=Profile)