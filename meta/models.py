from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Overview(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE,blank=True, null=True)
    video = models.FileField(upload_to='meta_video/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    requirement = models.TextField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.profile} ==> {self.title}"
    
    def get_profile_Picture(self):
        return self.profile.seller_profile.avatar

    def get_full_Name(self):
        return self.profile.seller_profile.full_Name

    def get_start_price(self):
        return self.meta_pricing.filter(packages="Basic").first().Price if self.meta_pricing.filter(packages="Basic").first() else "200"

    def get_url(self):
        return reverse("about_meta", kwargs={"query": self.id})

class search_keyword(models.Model):
    profile = models.ForeignKey(Overview, on_delete=models.CASCADE, blank=True, null=True, related_name = "keyword")
    search_keyword = models.CharField(max_length=700, blank=True, null=True)
    def __str__(self) -> str:
        return self.search_keyword 

class Pricing(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True, related_name="meta_pricing")
    packages = models.CharField(max_length=20, blank=True, null=True)
    heading = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    Price = models.FloatField(blank=True, null=True)
    delivery_time = models.IntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return self.packages

class Service_offer(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    Price = models.ForeignKey(Pricing,on_delete=models.CASCADE, blank=True, null=True)
    service_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self) -> str:
        return self.Price.packages

class FAQ(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    question = models.CharField(max_length=70, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
        return self.question

class Gallery(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    Picture = models.ImageField(upload_to='meta_images/', null=True, blank=True)


class Pdf(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    project = models.FileField(upload_to='pdf/', null=True, blank=True)


class Publish(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    progress = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)
    suspend_message = models.CharField(max_length=70, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now = True, blank=False, null=False)
    last_modified = models.DateTimeField(auto_now_add=True, blank=False, null=False)


    def __str__(self):
        return f"{self.publish_date.now()} ==> {self.last_modified.now()}"
    