from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date


# Create your models here.
class User(AbstractUser):

  def __str__(self):
    return self.username

class Goal(models.Model):
  name = models.CharField(max_length = 100)
  created_at = models.DateField(default=date.today)
  user = models.ForeignKey(to="User", related_name="goals", on_delete=models.CASCADE)
  CHOICES = [ ('fewer than', 'fewer than'),
  ('more than', 'more than'), 
  ('at least','at least'),
  ('at most', 'at most'),
  ('exactly', 'exactly') ]
  operator = models.CharField(max_length=10, choices=CHOICES)
  numeric_goal = models.PositiveIntegerField()
  units = models.CharField(max_length = 100, null=True, blank=True)

  def __str__(self):
    return self.name

class History(models.Model):
  goal = models.ForeignKey(to="Goal", related_name="goal", on_delete=models.CASCADE)
  daily_input = models.PositiveIntegerField(default=0)
  day_of_input = models.DateField(default=date.today)
  target = models.PositiveIntegerField()
  
  def save(self, *args, **kwargs):
    if self.target is None:
      self.target = self.goal.numeric_goal
      super().save(*args, **kwargs)
      return self.target

  def __str__(self):
    return f'Your input on {self.day_of_input} was {self.daily_input}. ' 