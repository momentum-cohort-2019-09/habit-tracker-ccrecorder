from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):

  def __str__(self):
    return self.username

class Goal(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(timezone.now())
  numeric_goal = models.IntegerField()
  user = models.ForeignKey(to="User", related_name="user", on_delete=models.CASCADE)
  CHOICES = [('<', 'less than'),
  ('>', 'more than'),
  ('>=', 'at least'),
  ('<=', 'at most'),
  ('=', 'exactly')]
  operator = models.CharField(max_length=10, choices=CHOICES)

  def __str__(self):
    return self.name

class History(models.Model):
  goal = models.ForeignKey(to="Goal", related_name="goal", on_delete=models.CASCADE)
  daily_input = models.IntegerField()
  day = models.DateField()
  
  def get_numeric_goal(self):
    target = self.goal.numeric_goal
    return target


