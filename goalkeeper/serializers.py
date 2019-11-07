from rest_framework import serializers
from goalkeeper.models import User, Goal, History

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email']

class GoalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Goal
    fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = History
    fields = '__all__'
