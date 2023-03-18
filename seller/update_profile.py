from django.contrib import messages
from seller.models import Personal_Info
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User

@csrf_exempt
def update_pics(request):
  if request.method == "POST":
    pics = json.loads(request.body.decode()).get("profile_pic")
    profile_obj, _ = Personal_Info.objects.get_or_create(profile_id=request.user.id)
    new_obj = Personal_Info.objects.update(id = profile_obj.id, avatar=pics)
  return JsonResponse({"response": "successfully updated profile pics"})

def update_profile(request):
  if request.method == "POST":
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    full_name = f"{first_name} {last_name}"
    email = request.POST.get("email")
    location = request.POST.get("location")
    profile_obj, _ = Personal_Info.objects.get_or_create(profile_id=request.user.id)
    Personal_Info.objects.update(id = profile_obj.id, full_Name=full_name, location=location)
    profile_obj.profile.email = email
    profile_obj.save()
    messages.success(request, "successfully updated profile")
    
  return redirect("setting")