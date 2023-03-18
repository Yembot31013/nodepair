from django.db import models
from django.contrib.auth.models import User

class Message_Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    subscribe = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.subject

class Header_video(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    video = models.FileField(upload_to='header_video/', null=True, blank=True)

    def __str__(self):
        return self.title

class Offers(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='offer/', null=True, blank=True)
    sub_image = models.ImageField(upload_to='offer/', null=True, blank=True)
    def __str__(self):
        return self.title

class About(models.Model):
    sub_description = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='offer/', null=True, blank=True)
    def __str__(self):
        return "about Us"

class Team(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    role = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    def __str__(self):
        return self.name

class Social_media(models.Model):
    name = models.URLField(max_length=1000, blank=True, null=True)
    name = models.URLField(max_length=1000, blank=True, null=True)
    name = models.URLField(max_length=1000, blank=True, null=True)
    name = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return "social Media"

class Available_Status(models.Model):
  profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="available_status")
  online = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now = True)

    

