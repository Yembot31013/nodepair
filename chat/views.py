from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound

from chat.models import Thread
from meta.models import Overview
from seller.models import Personal_Info
from projectApp.models import Project_Overview
from django.db.models import Max


@login_required(login_url="loginpage")
def home(request):
  if request.method == "POST":
    about_id = request.POST.get("about_id")
    about_type = request.POST.get("type")
    # if about_type == "project":
    #   project_obj = get_object_or_404(Project_Overview, pk=int(about_id))
    #   seller = project_obj.profile
    # elif about_type == "meta":
    #   meta_obj = get_object_or_404(Overview, pk=int(about_id))
    #   seller = meta_obj.profile
    # else:
    #   return HttpResponseNotFound()
    if about_type == "navbar":
      if request.user.id != int(about_id):
        try:
          thread_obj = Thread.objects.get(seller_id = int(about_id), buyer=request.user)
        except:
          thread_obj = Thread.objects.get(seller = request.user, buyer=int(about_id))

        unreadThread = thread_obj.chatMessage_thread.filter(unread=True)
        for i in unreadThread:
          i.unread = False
          i.save()

        threads = Thread.objects.by_user(user=request.user).annotate(max_t = Max("chatMessage_thread__timestamp")).order_by("-max_t").prefetch_related("chatMessage_thread")
        print(thread_obj)
        contexts = {
          "thread": threads,
          "Thread_obj": thread_obj,
        }
        return render(request, "chats/index.html", contexts)
    seller = get_object_or_404(Personal_Info, pk=int(about_id)).profile
    if request.user.id != int(about_id):
      thread_obj = Thread.objects.get_or_create(seller= seller, buyer=request.user)[0]

      threads = Thread.objects.by_user(user=request.user).annotate(max_t = Max("chatMessage_thread__timestamp")).order_by("-max_t").prefetch_related("chatMessage_thread")
      print(thread_obj)
      contexts = {
        "thread": threads,
        "Thread_obj": thread_obj,
      }
      return render(request, "chats/index.html", contexts)

  threads = Thread.objects.by_user(user=request.user).annotate(max_t = Max("chatMessage_thread__timestamp")).order_by("-max_t").prefetch_related("chatMessage_thread")
  context = {
    "thread": threads
  }
  return render(request, "chats/index.html", context)

