from rest_framework import serializers
from store.models import PetrolStore, Price, Service, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file',)


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('name', 'cost', 'currency', 'image')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'image')


class PetrolSerializer(serializers.ModelSerializer):

    prices = PriceSerializer(read_only=True, many=True)
    services = ServiceSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = PetrolStore
        fields = '__all__'
