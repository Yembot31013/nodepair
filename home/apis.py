from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, How_To_Pay
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

@api_view(["GET"])
def send(request, *arg, **kwarg):
  token = request.query_params.get("token")
  data = {}

  return Response({"status": "success"}, status=200)