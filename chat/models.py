from django.db import models
from django.db.models import Q

# Create your models here.
from django.contrib.auth.models import User

class ThreadManager(models.Manager):
  def by_user(self, **kwargs):
    user = kwargs.get("user")
    lookup = Q(seller = user)|Q(buyer = user)
    qs = self.get_queryset().filter(lookup).distinct()
    return qs


class Thread(models.Model):
  seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="thread_seller")
  buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="thread_buyer")
  updated_time = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = ThreadManager()

  def total_seller_unread(self, **kwargs):
    qs = self.chatMessage_thread.filter(user=self.seller, unread = True).count() # type: ignore
    return qs
    

  def total_buyer_unread(self, **kwargs):
    qs = self.chatMessage_thread.filter(user=self.buyer, unread = True).count()
    return qs
  
  def __str__(self):
    return f"{self.id}"
    

  class Meta:
    unique_together = ["seller", "buyer"]

class ChatMessage(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True, blank=True, related_name="chatMessage_thread")
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatMessage_from")
  to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatMessage_to", null=True)
  message = models.TextField()
  unread = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now_add = True)


class Status(models.Model):
  profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_status")
  online = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now = True)





