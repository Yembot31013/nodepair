from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from chat.models import ChatMessage
import random

class Personal_Info(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="seller_profile")
    full_Name = models.CharField(max_length=170, blank=True, null=True)
    avatar = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    location = models.CharField(max_length=700, blank=True, null=True)
    slogan = models.CharField(max_length=700, blank=True, null=True)
    is_seller = models.BooleanField(default=False, null=True, blank=True)
    seller_mode = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(max_length=40, blank=True, null=True, unique=True)
    impression = models.IntegerField(blank=True, null=True, default=0)

    

    def calculate_response_time(self):
        messages = ChatMessage.objects.filter(to_id=self.profile.id) # type: ignore
        response_times = []
        for message in messages:
            reply = ChatMessage.objects.filter(user_id=self.profile.id, timestamp__gt=message.timestamp).first() # type: ignore
            if reply:
                response_time = (reply.timestamp - message.timestamp).total_seconds()
                response_times.append(response_time)
        avg_response_time = sum(response_times) / len(response_times) if response_times else 0
        return avg_response_time // 3600


    def calculate_response_percentage(self):
        messages = ChatMessage.objects.filter(to_id=self.profile.id) # type: ignore
        response_times = []
        total_messages = messages.count()
        if total_messages == 0:
            return 100
        for message in messages:
            reply = ChatMessage.objects.filter(user_id=self.profile.id, timestamp__gt=message.timestamp).first() # type: ignore
            if reply:
                response_time = (reply.timestamp - message.timestamp).total_seconds()
                response_times.append(response_time)
        response_percentage = len(response_times) / total_messages * 100
        return response_percentage

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_name = slugify(self.full_Name, allow_unicode=True) # type: ignore
            slug_obj = Personal_Info.objects.filter(slug = slug_name)
            while slug_obj:
                print("in_loop: ", slug_name)
                num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                num = list(map(str, num)) # type: ignore
                alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "x", "t", "u", "v", "w", "x", "y", "z"]
                alphanum = num + alpha
                randomValue = random.choices(alphanum, k=4)
                randomValue = "".join(randomValue) # type: ignore
                slug_name = slugify(self.full_Name, allow_unicode=True) # type: ignore
                slug_name = f"{slug_name}-{randomValue}"
                slug_obj = Personal_Info.objects.filter(slug = slug_name)
            print("out_of_loop: ", slug_name)
            self.slug = slug_name
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.full_Name
    


class Language_Levels(models.Model):
    language = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.language # type: ignore

class Skill_Levels(models.Model):
    skill_level = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.skill_level # type: ignore

class Languages(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length=70, null=True, blank=True)
    Language_Levels = models.ForeignKey(Language_Levels, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.language # type: ignore

class Occupation_list(models.Model):
    occupations = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.occupations # type: ignore

class Occupation(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    occupation = models.ForeignKey(Occupation_list, on_delete=models.CASCADE)
    from_year = models.IntegerField(null=True, blank=True)
    to_year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.occupation.occupations # type: ignore

class Skill_list(models.Model):
    skiller = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.skiller # type: ignore

class Skill(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.ForeignKey(Skill_list, on_delete=models.CASCADE) # type: ignore
    level = models.ForeignKey(Skill_Levels, on_delete=models.CASCADE) # type: ignore

    def __str__(self) -> str:
        return self.skills.skiller # type: ignore

class Education(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True) # type: ignore
    country = models.CharField(max_length=700, null=True, blank=True)
    name = models.CharField(max_length=700, null=True, blank=True)
    title = models.CharField(max_length=700, null=True, blank=True)
    major = models.CharField(max_length=700, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.major # type: ignore

class Certification(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True) # type: ignore
    Certificate = models.CharField(max_length=700, null=True, blank=True)
    certified = models.CharField(max_length=700, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.Certificate # type: ignore

class Professional_Info(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True) # type: ignore
    personal_Website = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile.full_Name # type: ignore

class Linked_Accounts(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True) # type: ignore
    Google = models.URLField(blank=True, null=True)
    Facebook = models.URLField(blank=True, null=True)
    Twitter = models.URLField(blank=True, null=True)
    Github = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile.full_Name # type: ignore

class Account_Security(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    phone_Number = models.IntegerField(blank=True, null=True)
    is_verified = models.BooleanField(blank=True, null=True, default=False)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile.full_Name # type: ignore
