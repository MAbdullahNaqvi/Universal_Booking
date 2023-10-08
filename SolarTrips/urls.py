from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('login',views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('planet/<int:id>', views.planet, name="planet"),
    path("packages", views.packages, name="packages"),
    path("wishlist", views.wishlist, name="wishlist")
]