from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal_Info
from chat.models import ChatMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboard.models import Meta_Order
# from dashboard.models import Project_Order
from projectApp.models import Project_Overview
from django.db import models

# Create your views here.

def is_node(user):
  if Personal_Info.objects.filter(profile = user):
    return user.seller_profile.seller_mode
  return True

# @login_required(login_url="loginpage")
def seller_info(request, name):
  pl = get_object_or_404(Personal_Info, slug = name)
  user_info = pl.profile
  meta = user_info.overview_set.all() # type: ignore
  project = user_info.project_overview_set.all() # type: ignore
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count() # type: ignore
  context = {
    "profile": pl,
    "meta": meta,
    "project": project,
    "pending_count": pending_count,
    "chatMsg": chatMsg
  }

  return render(request, "profile/seller_details.html", context)


@login_required(login_url="loginpage")
def home(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  context = {
    "profile": pl,
    "pending_count": pending_count,
    "chatMsg": chatMsg
  }
  return render(request, "nodeDashboard/nodeHome.html", context)

@login_required(login_url="loginpage")
def dashboard(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  metaOrder = Meta_Order.objects.filter(seller_id = pl.id).order_by("-created_at")[:5]
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  context = {
    "profile": pl,
    "pending_count": pending_count,
    "metaOrder": metaOrder,
    "chatMsg": chatMsg
  }
  return render(request, "nodeDashboard/nodeDashboard.html", context)

@login_required(login_url="loginpage")
def order(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  metaOrder = Meta_Order.objects.filter(seller_id = pl.id).order_by("-created_at")

  complete_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Completed").count()
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  cancel_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Cancelled").count()
  decline_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Decline").count()
  decline_cancel_count = cancel_count + decline_count
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  context = {
    "profile": pl,
    "chatMsg": chatMsg,
    "metaOrder": metaOrder,
    "complete_count": complete_count,
    "pending_count": pending_count,
    "decline_cancel_count": decline_cancel_count,
  }
  return render(request, "nodeDashboard/nodeOrder.html", context)

@login_required(login_url="loginpage")
def product(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  meta = request.user.overview_set.all()
  project = request.user.project_overview_set.all()
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  context = {
    "profile": pl,
    "meta": meta,
    "pending_count": pending_count,
    "project": project,
    "chatMsg": chatMsg
  }
  return render(request, "nodeDashboard/nodeProduct.html", context)

@login_required(login_url="loginpage")
def customer(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  context = {
    "profile": pl,
    "pending_count": pending_count,
    "chatMsg": chatMsg
  }
  return render(request, "nodeDashboard/nodeCustomer.html", context)

@login_required(login_url="loginpage")
def iframeTab(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  context = {
    "profile": pl,
    "pending_count": pending_count,
    "chatMsg": chatMsg
  }
  return render(request, "nodeDashboard/iframe.html", context)

@login_required(login_url="loginpage")
def chatbot(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  if not pl.seller_mode:
    return redirect("/")
  chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("-timestamp")
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count() # type: ignore
  context = {
    "profile": pl,
    "pending_count": pending_count,
    "chatMsg": chatMsg
  }
  return render(request, "nodeDashboard/trainChatBot.html", context)

@login_required(login_url="loginpage")
def settings(request):
  pl = get_object_or_404(Personal_Info, profile_id = request.user.id)
  total_unread = ChatMessage.objects.filter(to_id = request.user.id, unread = True).count()
  pending_count = Meta_Order.objects.filter(seller_id = pl.id, status = "Pending").count()
  context = {
    "profile": pl,
    "pending_count": pending_count,
    "total_unread": total_unread,
  }
  return render(request, "nodeDashboard/settings.html", context)