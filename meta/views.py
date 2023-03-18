from django.shortcuts import render
from meta.models import Overview
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MetaSerializer

class fetchMeta(generics.ListAPIView):
  queryset = Overview.objects.all()[:3]
  serializer_class = MetaSerializer

class fetchRateMeta(generics.ListAPIView):
  queryset = Overview.objects.all()[:3]
  serializer_class = MetaSerializer


@api_view(['GET'])
def metaDetailApiView(request, query=None, *args, **kwargs):
  queryset = Overview.objects.filter(title__contains=query, keyword__search_keyword__contains=query).order_by("progress")
  data = MetaSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def productMeta(request, query=None, *args, **kwargs):
  queryset = Overview.objects.filter(profile = request.user)
  data = MetaSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def profileMeta(request, query=None, *args, **kwargs):
  print("query", query)
  queryset = Overview.objects.filter(profile_id=query).order_by("created")
  data = MetaSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def recommendedMeta(request, *args, **kwargs):
  queryset = Overview.objects.all().order_by("progress")
  data = MetaSerializer(queryset, many=True).data
  return Response(data)

@api_view(['GET'])
def rateMeta(request, *args, **kwargs):
  queryset = Overview.objects.all().order_by("progress")
  data = MetaSerializer(queryset, many=True).data
  return Response(data)




