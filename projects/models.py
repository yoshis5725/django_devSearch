from django.db import models
import uuid


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)  # can submit and leave this field empty
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')  # installed pillow
    demo_link = models.CharField(max_length=256, null=True, blank=True)
    source_link = models.CharField(max_length=256, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # auto generating a timestamp

    # relationships
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=32, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    # relationships
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # one-to-many relation to the Projects model

    def __str__(self):
        return f'{self.value}'


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
