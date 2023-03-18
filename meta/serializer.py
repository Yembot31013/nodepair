from .models import Overview
from rest_framework import serializers

class MetaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Overview
    fields = [
      "video",
      "title",
      "get_profile_Picture",
      "get_full_Name",
      "get_start_price",
      "get_url",
    ]
