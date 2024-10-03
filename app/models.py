from django.db import models


class City(models.Model):
    """場所"""

    name = models.CharField("name", max_length=20)

    def __str__(self):
        return self.name


class Week(models.Model):
    """週情報"""

    city_id = models.IntegerField("city_id", unique=True)
    order = models.IntegerField("order")
    sunday = models.IntegerField("sunday")
    monday = models.IntegerField("monday")
    tuesday = models.IntegerField("tuesday")
    wednesday = models.IntegerField("wednesday")
    thursday = models.IntegerField("thursday")
    friday = models.IntegerField("friday")
    saturday = models.IntegerField("saturday")

    def __str__(self):
        return f"{self.sunday} {self.monday} {self.tuesday} {self.wednesday} {self.thursday} {self.friday} {self.saturday}"
