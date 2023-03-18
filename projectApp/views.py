from django.shortcuts import render
from projectApp.models import Project_Overview
from rest_framework import generics
from .serializer import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class fetchProject(generics.ListAPIView):
  queryset = Project_Overview.objects.all()[:3]
  serializer_class = ProjectSerializer

class fetchRateProject(generics.ListAPIView):
  queryset = Project_Overview.objects.all()[:3]
  serializer_class = ProjectSerializer

@api_view(['GET'])
def profileProject(request, query=None, *args, **kwargs):
  queryset = Project_Overview.objects.filter(profile_id=query).order_by("created")
  data = ProjectSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def productProject(request, query=None, *args, **kwargs):
  queryset = Project_Overview.objects.filter(profile=request.user)
  data = ProjectSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def projectDetailApiView(request, query=None, *args, **kwargs):
  queryset = Project_Overview.objects.filter(title__contains=query, keyword__search_keyword__contains=query).order_by("progress")
  data = ProjectSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def recommendedProject(request, *args, **kwargs):
  queryset = Project_Overview.objects.all().order_by("progress")
  data = ProjectSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def rateProject(request, *args, **kwargs):
  queryset = Project_Overview.objects.all().order_by("progress")
  data = ProjectSerializer(queryset, many=True).data
  return Response(data)


