from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import User, planets, destination
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, logout, get_user, authenticate


def index(request):
    planet = planets.objects.all()
    return render(request,"SolarTrips/index.html",{
        "planets": planet
    })


def login_view(request):
    if request.method == "POST":
         # Attempt to sign user in
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "SolarTrips/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "SolarTrips/login.html")


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        email = request.POST["email"]
        
        if password != confirm:
            return render(request,"SolarTrips/register.html", {
                "message": "Passwords Dont Match"
            })

        try:
            new_user = User.objects.create_user(name, email, password)
            new_user.save()
        except IntegrityError:
            return render(request, "SolarTrips/register.html", {
                "message": "Username already taken."
            })
        login(request, new_user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "SolarTrips/register.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def planet(request, id):
    planet = planets.objects.get(id = id)
    destinations = destination.objects.filter(planet = planet)
    if request.method == "POST":
        book = request.POST.get("Booked", False)
        cancel_book = request.POST.get("cancel_Booked", False)
        wishlist = request.POST.get("wishlist", False)
        cancel_wishlist = request.POST.get("cancel_wishlist", False)
        if book != False:
            planet.passengers.add(request.user)
            planet.save
            return HttpResponseRedirect(f"/planet/{id}")
        elif wishlist != False:
            planet.wishlist.add(request.user)
            planet.save
            return HttpResponseRedirect(f"/planet/{id}")
        elif cancel_book != False:
            planet.passengers.remove(request.user)
            planet.save
            return HttpResponseRedirect(f"/planet/{id}")
        elif cancel_wishlist != False:
            planet.wishlist.remove(request.user)
            planet.save
            return HttpResponseRedirect(f"/planet/{id}")
    else:
        return render(request,"SolarTrips/planet.html",{
            "planet": planet,
            "destinations": destinations
        })

@login_required
def packages(request):
    packages = planets.objects.filter(passengers = request.user)
    return render(request, "SolarTrips/packages.html",{
        "packages": packages
    })

@login_required
def wishlist(request):
    wishlist = planets.objects.filter( wishlist = request.user)
    return render(request, "SolarTrips/wishlist.html",{
        "packages": wishlist
    })