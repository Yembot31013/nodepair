from rest_framework.response import Response
from seller.models import Language_Levels, Occupation_list, Skill_list, Skill_Levels
from meta.models import Category, Sub_Category
from rest_framework import generics
from .serializer import LanguageSerializer, OccupationSerializer, SkillSerializer, SkillLevelSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.decorators import api_view
import random

def get_random_code():
  num = 0
  count = 8
  rand = ""
  while num < count:
    ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    rand += str(ran)
    num += 1

  return rand

@api_view(['GET'])
def search_language(request, *args, **kwargs):
  queryset = Language_Levels.objects.all()
  data = LanguageSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def search_occupation(request, *args, **kwargs):
  queryset = Occupation_list.objects.all()
  data = OccupationSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def search_skill(request, *args, **kwargs):
  queryset = Skill_list.objects.all()
  data = SkillSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def skill_level(request, *args, **kwargs):
  queryset = Skill_Levels.objects.all()
  data = SkillLevelSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def search_category(request, *args, **kwargs):
  queryset = Category.objects.all()
  data = CategorySerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def search_subcategory(request, *args, **kwargs):
  obj = Category.objects.filter(name = request.GET.get("category")).first()
  if obj:
    queryset = Sub_Category.objects.filter(category = obj)
    data = SubCategorySerializer(queryset, many=True).data
    return Response(data)
  return Response({})

