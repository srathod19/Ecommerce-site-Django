from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path("shop", views.index, name="shop"),
    path("contact", views.contact, name="contact"),
    path("login", views.loginUser, name="login"),
    # path("about", views.about, name="AboutUs"),
    path("tracker", views.tracker, name="TrackingStatus"),
    path("search", views.search, name="Search"),
    path("product/<int:myid>", views.productview, name="product"),
    path("checkout", views.checkout, name="CheckOut"),
    path("signup", views.signup, name="signup"),
    path('logout', views.logoutUser, name="logout"),
    path('cart', views.cart, name="cart"),
    path("category", views.Category, name="Category")
]
