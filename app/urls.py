from django.urls import path
from app import views

app_name = "app"
urlpatterns = [
    path("", views.top, name="index"),
    path("detail/<int:city_id>", views.detail, name="detail"),
]
