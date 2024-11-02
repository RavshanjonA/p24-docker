from django.urls import path
from .api_endpoints import group
urlpatterns = [
    path('group/', group.GroupListCreateView.as_view(), name='groups'),
    path('group/<pk>/', group.GroupRetrieveUpdateDestroyView.as_view(), name='group')
]