import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from seller.models import Personal_Info, Occupation_list, Languages, Professional_Info, Language_Levels, Occupation, Skill_list, Skill, Skill_Levels
from meta.models import Overview, Gallery, Pdf, search_keyword, Category, Sub_Category, FAQ, Pricing, Service_offer, Publish
from projectApp.models import Project_Overview, Project_Gallery, Project_Project, Project_search_keyword, Project_Category, Project_Sub_Category, Project_FAQ, Project_Pricing, Project_Publish
import random
import json

def get_random_code():
  num = 0
  count = 8
  rand = ""
  while num < count:
    ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    rand += str(ran)
    num += 1

  return rand

@login_required(login_url="loginpage")
def create_profile(request):
    fullname = request.POST.get("info[fullname]", None)
    picture = request.POST.get("info[profile_pics]", None)
    description = request.POST.get("info[description]", None)
    url = request.POST.get("info[url]", None)
    occup = request.POST.get("occup", None)
    skill = request.POST.get("skill", None)
    langs = request.POST.get("language", None)
    slogan = request.POST.get("info[slogan]", None)


    if fullname is None:
      return JsonResponse({"status": "Full name is required"})

    sell = Personal_Info(profile=request.user, full_Name=fullname, avatar=picture, description=description, is_seller=True, seller_mode=True, slogan=slogan)
    sell.save()

    if url:
      web = Professional_Info(profile=sell, personal_Website=url)
      web.save()
    # print(sell)
    #language = sell.languages_set.all()
    if langs:
      for i in range(int(langs)):
        info_name = request.POST.get(f"info[language][{i}][name]", None)
        info_level = request.POST.get(f"info[language][{i}][level]", None)
        lang_obj = Language_Levels.objects.get(language=info_level)
        lang = Languages(profile=sell, language=info_name, Language_Levels=lang_obj)
        lang.save()
    if skill:
      for i in range(int(skill)):
        skill_name = request.POST.get(f"info[skills][{i}][skill]", None)
        skill_level = request.POST.get(f"info[skills][{i}][level]", None)
        skills = Skill_list.objects.get(skiller=skill_name)
        lev_obj = Skill_Levels.objects.get(skill_level=skill_level)
        ins_skill = Skill(profile=sell, skills=skills, level=lev_obj)
        ins_skill.save()
    if occup:
      for i in range(int(occup)):
        occupation_name = request.POST.get(f"info[occupation][{i}][occup]", None)
        occupation_from = request.POST.get(f"info[occupation][{i}][fyear]", None)
        occupation_to = request.POST.get(f"info[occupation][{i}][tyear]", None)
        occp_obj = Occupation_list.objects.get(occupations=occupation_name)
        occp = Occupation(profile = sell, occupation= occp_obj, from_year=occupation_from, to_year=occupation_to)
        occp.save()

    return JsonResponse({"status": "success"})
  

@login_required(login_url="loginpage")
def submitProjects(request):
    if request.method == "POST":
        print(dir(request.user_agent))
        print(request.user_agent.get_os())
        print(request.user_agent.is_bot)
        print(request.user_agent.get_device())
        data = request.POST.get('data')
        video = request.FILES.get('videoInput')
        img1 = request.FILES.get('img1Input')
        img2 = request.FILES.get('img2Input')
        img3 = request.FILES.get('img3Input')
        project = request.FILES.get('projectInput')
        data = json.loads(data)
        projects = Project_Overview(profile=request.user)
        projects.title = data.get("projectTitle")
        cat = Project_Category.objects.get(name=data.get("category"))
        projects.category = cat
        scat = Project_Sub_Category.objects.get(category = cat, name=data.get("subCategory"))
        projects.sub_category = scat
        projects.video = video
        projects.description = data.get("description")
        projects.save()

        for i in data.get("FAQ").keys():
          question = data["FAQ"][i]["question"]
          answer = data["FAQ"][i]["answer"]
          faq = Project_FAQ(profile = projects, question=question, answer=answer)
          faq.save()

        for i in data.get("searchTag"):
          sk = Project_search_keyword(profile = projects, search_keyword = i)
          sk.save()

        price = Project_Pricing(profile = projects)
        price.color = data.get("color")
        price.Price = data.get("price")
        price.discount = data.get("discount")
        price.save()

        if img1:
          gallery = Project_Gallery(profile = projects)
          gallery.Picture = img1
          gallery.save()
        if img2:
          gallery = Project_Gallery(profile = projects)
          gallery.Picture = img2
          gallery.save()
        if img3:
          gallery = Project_Gallery(profile = projects)
          gallery.Picture = img3
          gallery.save()

        if project:
          pdf = Project_Project(profile = projects)
          pdf.project = project
          pdf.save()

        pub = Project_Publish(profile = projects, publish=True, publish_date=datetime.datetime.now(), last_scan = datetime.datetime.now())
        pub.save()

        return redirect("product")
    return redirect("/")

@login_required(login_url="loginpage")
def create_meta(request):
  if request.method == "POST":
    print(dir(request.user_agent))
    print(request.user_agent.get_os())
    print(request.user_agent.is_bot)
    print(request.user_agent.get_device())
    data = request.POST.get('data')
    video = request.FILES.get('videoInput')
    img1 = request.FILES.get('img1Input', None)
    img2 = request.FILES.get('img2Input', None)
    img3 = request.FILES.get('img3Input', None)
    pdf1 = request.FILES.get('pdf1Input', None)
    pdf2 = request.FILES.get('pdf2Input', None)
    data = json.loads(data)
    meta = Overview(profile = request.user)
    meta.title = data.get("projectTitle")
    cat = Category.objects.get(name=data.get("category"))
    meta.category = cat
    scat = Sub_Category.objects.get(category = cat, name=data.get("subCategory"))
    meta.sub_category = scat
    meta.video = video
    meta.description = data.get("description")
    meta.requirement = data.get("requiredNote")
    meta.save()

    for i in data.get("priceValue").keys():
      payType = data["priceValue"][i]["payType"]
      payHead = data["priceValue"][i]["payHead"]
      colorValue = data["priceValue"][i]["colorValue"]
      price = data["priceValue"][i]["price"]
      duration = data["priceValue"][i]["duration"]
      price_obj = Pricing(profile = meta, packages = payType, heading = payHead, color = colorValue, Price = price, delivery_time = duration)
      price_obj.save()
      for i in data["priceValue"][i]["serviceValue"]:
        each_service_obj = Service_offer(profile = meta, Price = price_obj, service_name = i)
        each_service_obj.save()

    for i in data.get("FAQ").keys():
      question = data["FAQ"][i]["question"]
      answer = data["FAQ"][i]["answer"]
      faq = FAQ(profile = meta, question=question, answer=answer)
      faq.save()

    for i in data.get("searchTag"):
      sk = search_keyword(profile = meta, search_keyword = i)
      sk.save()

    if img1:
      gallery = Gallery(profile = meta)
      gallery.Picture = img1
      gallery.save()
    if img2:
      gallery = Gallery(profile = meta)
      gallery.Picture = img2
      gallery.save()
    if img3:
      gallery = Gallery(profile = meta)
      gallery.Picture = img3
      gallery.save()

    if pdf1:
      pdf = Pdf(profile = meta)
      pdf.project = pdf1
      pdf.save()

    if pdf2:
      pdf = Pdf(profile = meta)
      pdf.project = pdf2
      pdf.save()
    
    pub = Publish(profile = meta, publish=True)
    pub.save()

    return redirect("product")

  return redirect("/")