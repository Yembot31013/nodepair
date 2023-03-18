from .models import Project_Overview
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project_Overview
    fields = [
      "video",
      "title",
      "get_profile_Picture",
      "get_full_Name",
      "get_start_price",
      "get_url",
    ]