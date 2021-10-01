from django.db import models


class House(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True, auto_created=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    housing_median_age = models.FloatField()
    total_rooms = models.FloatField()
    total_bedrooms = models.FloatField()
    population = models.FloatField()
    households = models.FloatField()
    median_income = models.FloatField()
    median_house_value = models.FloatField()
    ocean_proximity = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.id}'

    class Meta:
        db_table = "houses"