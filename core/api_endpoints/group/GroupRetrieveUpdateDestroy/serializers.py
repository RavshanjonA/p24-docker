from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer


class GroupRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
