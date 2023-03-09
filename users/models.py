from django.db import models
from django.contrib.auth.models import User  # using this to copy the attributes into the profile
import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    intro = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=128, blank=True, null=True)
    social_twitter = models.CharField(max_length=128, blank=True, null=True)
    social_linkedin = models.CharField(max_length=128, blank=True, null=True)
    social_youtube = models.CharField(max_length=128, blank=True, null=True)
    social_website = models.CharField(max_length=128, blank=True, null=True)

    # relationships
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)




