from rest_framework import serializers
from .models import House as house


class HouseSerializer(serializers.Serializer):
    id = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    housing_median_age = serializers.CharField()
    total_rooms = serializers.CharField()
    total_bedrooms = serializers.CharField()
    population = serializers.CharField()
    households = serializers.CharField()
    median_income = serializers.CharField()
    median_house_value = serializers.CharField()
    ocean_proximity = serializers.CharField()

    class Meta:
        model = house
        fields = '__all__'

    def create(self, validated_data):
        return house.objects.create(**validated_data)

    def update(self, instance, validated_data):
        house.objects.filter(pk=instance.id).update(**validated_data)