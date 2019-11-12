from django import forms
from .models import User, Goal, History

class GoalForm(forms.ModelForm):
  class Meta:
    model = Goal
    fields = ['name', 'operator', 'numeric_goal']