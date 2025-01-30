from rest_framework import serializers
from account.models import Data



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'