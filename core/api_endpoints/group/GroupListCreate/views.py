from django.contrib.auth.models import Group
from rest_framework.generics import ListCreateAPIView

from core.api_endpoints.group.GroupListCreate.serializers import GroupListCreateSerializer


class GroupListCreateView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListCreateSerializer


__all__ = ('GroupListCreateView',)
