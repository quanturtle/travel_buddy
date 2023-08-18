from django.urls import path
from travel.views import *

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('travels/', list_travel, name="list_travel"),
    path('travels/add/', add_travel, name="add_travel"),
    path('travels/destination/<int:pk>/', detail_travel, name="detail_travel"),
    path('travels/destination/<int:pk>/join/', join_travel, name="join_travel"),
]
