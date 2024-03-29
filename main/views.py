from django.shortcuts import render, redirect
from main.models import aboutAdmin, adminService
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def render_index_page(request):
    user = request.user
    if user.is_anonymous:
        user_data = {"user_name": "anon", "full_name": "Anonymouse User"}
    elif user.is_authenticated:
        user_data = {
            "user_name": user.username,
            "full_name": user.first_name + " " + user.last_name,
        }
    else:
        pass
    return render(request, "main/index.html", {"user_data": user_data})


def render_about_page(request):
    user = request.user
    if user.is_anonymous:
        user_data = {"user_name": "anon", "full_name": "Anonymouse User"}
    elif user.is_authenticated:
        user_data = {
            "user_name": user.username,
            "full_name": user.first_name + " " + user.last_name,
        }
    else:
        pass
    aAdmin = aboutAdmin.objects.all()[0]  # there must be one admin and using [0] so...
    about_data = {
        "name": aAdmin.name,
        "desc": aAdmin.description,
        "bday": aAdmin.birthday,
        "website": aAdmin.website,
        "phone": aAdmin.phone,
        "city": aAdmin.city,
        "age": aAdmin.age,
        "degree": aAdmin.degree,
        "email": aAdmin.email,
        "freelance": aAdmin.freelance,
        "interest_list": [i.strip() for i in aAdmin.interestes.split(",") if i != ""],
    }
    return render(
        request,
        "main/about.html",
        {"about_data": about_data, "user_data": user_data},
    )


def render_contact_page(request):
    user = request.user
    if user.is_anonymous:
        user_data = {"user_name": "anon", "full_name": "Anonymouse User"}
    elif user.is_authenticated:
        user_data = {
            "user_name": user.username,
            "full_name": user.first_name + " " + user.last_name,
        }
    else:
        pass
    return render(request, "main/contact.html", {"user_data": user_data})


def render_services_page(request):
    obj = adminService.objects.all()[0]
    data = {
        "serviceListMajor": [
            i.strip() for i in obj.serviceNameMajor.split(",") if i != ""
        ],
        "serviceListMinor": [
            i.strip() for i in obj.serviceNameMinor.split(",") if i != ""
        ],
    }
    return render(request, "main/services.html", {"serviceData": data})


def render_allprojects_page(request):
    user = request.user
    if user.is_anonymous:
        user_data = {"user_name": "anon", "full_name": "Anonymouse User"}
    elif user.is_authenticated:
        user_data = {
            "user_name": user.username,
            "full_name": user.first_name + " " + user.last_name,
        }
    else:
        pass
    return render(request, "main/allprojects.html", {"user_data": user_data})


def registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "main/registration.html", {"form": form})


def userLogin(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            pass
        else:
            password = request.POST["password"]
            user_name = request.POST["username"]
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect("main:index_page_url")
            return redirect("main:login_page_url")
    else:
        return render(request, "main/login.html")


def userLogout(request):
    logout(request)
    return redirect("main:index_page_url")
