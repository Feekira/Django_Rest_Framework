from rest_framework import routers, serializers
from .models import Client

# Serializers define the API representation.
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','name','adress','age')