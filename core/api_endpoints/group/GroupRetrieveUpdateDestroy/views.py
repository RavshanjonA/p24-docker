from django.contrib.auth.models import Group
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from core.api_endpoints.group.GroupRetrieveUpdateDestroy.serializers import GroupRetrieveUpdateDestroySerializer


class GroupRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Group
    serializer_class = GroupRetrieveUpdateDestroySerializer


__all__ = ('GroupRetrieveUpdateDestroyView',)
