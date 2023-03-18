from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Project_Category(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Project_Sub_Category(models.Model):
    category = models.ForeignKey(Project_Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Project_Overview(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Project_Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(Project_Sub_Category, on_delete=models.CASCADE,blank=True, null=True)
    video = models.FileField(upload_to='project_video/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.profile} ==> {self.title}"

    def get_profile_Picture(self):
        return self.profile.seller_profile.profile_Picture

    def get_full_Name(self):
        return self.profile.seller_profile.full_Name

    def get_start_price(self):
        return self.project_pricing.all().first().Price if self.project_pricing.all().first() else "200"

    def get_url(self):
        return reverse("about_meta", kwargs={"query": self.id})

class Project_search_keyword(models.Model):
    profile = models.ForeignKey(Project_Overview, on_delete=models.CASCADE, blank=True, null=True, related_name="keyword")
    search_keyword = models.CharField(max_length=700, blank=True, null=True)
    def __str__(self) -> str:
        return self.search_keyword 

class Project_Pricing(models.Model):
    profile = models.ForeignKey(Project_Overview,on_delete=models.CASCADE, blank=True, null=True, related_name="project_pricing")
    color = models.CharField(max_length=20, blank=True, null=True)
    Price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    def __str__(self) -> str:
        return self.Price

class Project_FAQ(models.Model):
    profile = models.ForeignKey(Project_Overview,on_delete=models.CASCADE, blank=True, null=True)
    question = models.CharField(max_length=70, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
        return self.question

class Project_Gallery(models.Model):
    profile = models.ForeignKey(Project_Overview,on_delete=models.CASCADE, blank=True, null=True)
    Picture = models.ImageField(upload_to='project_images/', null=True, blank=True)


class Project_Project(models.Model):
    profile = models.ForeignKey(Project_Overview,on_delete=models.CASCADE, blank=True, null=True)
    project = models.FileField(upload_to='project/', null=True, blank=True)


class Project_Publish(models.Model):
    profile = models.ForeignKey(Project_Overview,on_delete=models.CASCADE, blank=True, null=True)
    progress = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)
    suspend_message = models.CharField(max_length=70, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now = True, blank=False, null=False)
    last_scan = models.DateTimeField(auto_now_add=True, blank=False, null=False)


    def __str__(self):
        return f"{self.publish_date} ==> {self.last_scan}"
    