from goalkeeper.models import User, Goal, History
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GoalSerializer, HistorySerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = UserSerializer

class GoalViewSet(viewsets.ModelViewSet):
  queryset = Goal.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = GoalSerializer

class HistoryViewSet(viewsets.ModelViewSet):
  queryset = History.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = HistorySerializer