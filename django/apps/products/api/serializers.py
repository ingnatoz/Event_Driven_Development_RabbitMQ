from rest_framework import serializers
from apps.products.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserTestSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        # print(instance)
        class Meta:
            model = User

        return {
            'id': instance['id'],
        }
