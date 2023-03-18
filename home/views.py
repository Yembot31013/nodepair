from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import CustomUserForm
from .models import Message_Feedback
from seller.models import Personal_Info
from meta.models import Pricing, Overview
from projectApp.models import Project_Overview
from chat.models import ChatMessage


def query_search(request, query):
    pl = Personal_Info.objects.filter(profile_id = request.user.id).first()
    metaqueryset = Overview.objects.filter(title__contains=query, keyword__search_keyword__contains=query).order_by("progress")
    projectqueryset = Project_Overview.objects.filter(title__contains = query, keyword__search_keyword__contains=query).order_by("progress")
    chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("timestamp")
    data = ""
    context = {
        "metaqueryset": metaqueryset,
        "projectqueryset": projectqueryset,
        "query": query,
        "profile": pl,
        "chatMsg": chatMsg,
    }
    return render(request, "homes/query.html", context)

def showMore(request, show):
    pl = Personal_Info.objects.filter(profile_id = request.user.id).first()
    if show == "rec_meta":
        moreData = Overview.objects.all()
    elif show == "rec_project":
        moreData = Project_Overview.objects.all()
    elif show == "rate_meta":
        moreData = Overview.objects.all()
    elif show == "rate_project":
        moreData = Project_Overview.objects.all()
    chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("timestamp")
    context={
            "moreData": moreData,
            "show": show,
            "profile": pl,
            "chatMsg": chatMsg,
        }
    return render(request, "homes/show.html", context)

def home(request):
    if request.user.is_authenticated:
        if Personal_Info.objects.filter(profile_id = request.user.id, seller_mode=True):
            return redirect('home')
        pl = Personal_Info.objects.filter(profile_id = request.user.id).first()
        meta_rec_queryset = Overview.objects.all()[:3]
        project_rec_queryset = Project_Overview.objects.all()[:3]
        meta_rate_queryset = Overview.objects.all()[:3]
        project_rate_queryset = Project_Overview.objects.all()[:3]
        chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("timestamp")
        context={
            "meta_rec_queryset": meta_rec_queryset,
            "project_rec_queryset": project_rec_queryset,
            "meta_rate_queryset": meta_rate_queryset,
            "project_rate_queryset": project_rate_queryset,
            "profile": pl,
            "chatMsg": chatMsg,
        }
        return render(request, "homes/index.html", context)
    
    return render(request, 'homes/home.html')
def about_meta(request, query):
    about_obj = get_object_or_404(Overview, pk=int(query))
    pl = Personal_Info.objects.filter(profile_id = request.user.id).first()
    print(about_obj.video)
    seller = Personal_Info.objects.filter(profile_id = about_obj.profile.id).first()
    chatMsg = ChatMessage.objects.filter(to_id = request.user.id, unread = True).order_by("timestamp")
    context = {
        "obj": about_obj,
        "profile": pl,
        "seller": seller,
        "chatMsg": chatMsg,
    }
    return render(request, "homes/about_meta.html", context)

def change(request):
    profile_obj = get_object_or_404(Personal_Info, profile_id = request.user.id)
    is_selling = profile_obj.seller_mode
    if is_selling:
        profile_obj.seller_mode = False
        profile_obj.save()
        return redirect("/")
    if not is_selling:
        profile_obj.seller_mode = True
        profile_obj.save()
        return redirect("/")

@login_required(login_url="loginpage")
def choice(request):
    if request.user_agent.is_mobile:
        return HttpResponse("<h1>you can only access this pages with a pc</h1>")
    return render(request, 'account/decisions.html')

@login_required(login_url="loginpage")
def payment_package(request, pay_id):
    pl = Personal_Info.objects.filter(profile_id = request.user.id).first()
    abt = Overview.objects.get(pk=pay_id)
    seller = Personal_Info.objects.filter(profile_id = abt.profile.id).first()
    price = abt.meta_pricing.all()
    context = {
        "about": abt,
        "profile": pl,
        "seller": seller,
        "objects": price
    }
    return render(request, 'about/payment/payment.html', context)

@login_required(login_url="loginpage")
def profile(request):
    if request.user_agent.is_mobile:
        return HttpResponse("<h1>you can only access this pages with a pc</h1>")
    return render(request, 'account/decision.html')

@login_required(login_url="loginpage")
def metas(request):
    if request.user_agent.is_mobile:
        return HttpResponse("<h1>you can only access this pages with a pc</h1>")
    some = Personal_Info.objects.filter(profile = request.user, is_seller=True)
    value = request.user
    context = {
        "u_token": value,
        "page": "meta"
    }
    if len(some) == 0:
        return render(request, 'profile/profile.html', context)
    return render(request, 'meta/meta.html', context)

@login_required(login_url="loginpage")
def projects(request):
    if request.user_agent.is_mobile:
        return HttpResponse("<h1>you can only access this pages with a pc</h1>")
    some = Personal_Info.objects.filter(profile = request.user, is_seller=True)
    value = request.user
    context = {
        "u_token": value,
        "page": "project"
    }
    if len(some) == 0:
        return render(request, 'profile/profile.html', context)
    return render(request, 'meta/project.html', context)



def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subcribe = request.POST.get('subcribe')
        if subject == "":
            return JsonResponse({"yemi": "Subject can't be empty, we will use your subject for our teams to response faster", "state": "info", "msg": "Info"})
        if email == "":
            return JsonResponse({"yemi": "Email can't be empty, we will need youe email to get back to you", "state": "info", "msg": "Info"})
        if message == "":
            return JsonResponse({"yemi": "Message can't be empty, message is important.", "state": "info", "msg": "Info"})
        if subcribe == "true":
            feedback = Message_Feedback(name=name, subject=subject, email=email, message=message, subscribe=True)
            feedback.save()
        else:
            feedback = Message_Feedback(name=name, subject=subject, email=email, message=message, subscribe=False)
            feedback.save()
        return JsonResponse({"yemi": "Subscribe Successfully", "state": "success", "msg": "Success"})

def register(request):
    redirect_link = request.GET.get("next", None)
    if redirect_link is not None:
        request.session["redirect_link"] = redirect_link
    
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'registered successfully! login to continue')
            return redirect('/login/')
    context = {'form': form}
    return render(request, 'account/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('/')
    else:
        if request.session.get("redirect_link"):
            redirect_link = request.session.get("redirect_link")
        else:
            redirect_link = request.GET.get("next", None)
            if redirect_link is not None:
                request.session["redirect_link"] = redirect_link
                redirect_link = request.session.get("redirect_link")
            else:
                redirect_link = "/"

        if request.method == 'POST':
            name = request.POST.get('username', None)
            passwd = request.POST.get('passwd', None)
            if name is not None and passwd is not None:
                user = authenticate(request, username=name, password=passwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in sucessfully')
                    return redirect(redirect_link)
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('/login/')
        return render(request, 'account/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
    return redirect('/')
