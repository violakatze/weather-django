from django.shortcuts import render
from .models import City, Week


def top(request):
    """トップページ"""
    message = {"title": "top"}
    return render(request, "index.html", message)


def detail(request, city_id):
    """詳細"""
    city = City.objects.get(pk=city_id)
    week = Week.objects.get(city_id=city.pk)
    forecasts = [
        week.sunday,
        week.monday,
        week.tuesday,
        week.wednesday,
        week.thursday,
        week.friday,
        week.saturday,
    ]
    day_of_weeks = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    message = {
        "title": city.name,
        "forecasts": forecasts,
        "day_of_weeks": day_of_weeks,
    }
    return render(request, "detail.html", message)
