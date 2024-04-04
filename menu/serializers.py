from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer): # may call this whatever, but typical syntax is ModelSerializer
    class Meta:
        model = Item
        fields = '__all__'