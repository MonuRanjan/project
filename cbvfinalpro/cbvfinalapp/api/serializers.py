from rest_framework import serializers
from cbvfinalapp.models import Beer

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = '__all__'