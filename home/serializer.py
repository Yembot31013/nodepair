from seller.models import Language_Levels, Occupation_list, Skill_list, Skill_Levels
from meta.models import Category, Sub_Category
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language_Levels
    fields = [
      "language"
    ]
class OccupationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Occupation_list
    fields = [
      "occupations"
    ]
class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill_list
    fields = [
      "skiller"
    ]
class SkillLevelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill_Levels
    fields = [
      "skill_level"
    ]

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = [
      "name"
    ]

class SubCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Sub_Category
    fields = [
      "name"
    ]