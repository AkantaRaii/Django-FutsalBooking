from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name="home"),
    path('createfutsal/',views.createfutsal,name="createfutsal"),
    path('signup',views.signup,name="signup")
    
]