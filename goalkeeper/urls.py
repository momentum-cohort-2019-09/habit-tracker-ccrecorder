from rest_framework import routers
from .api import UserViewSet, GoalViewSet, HistoryViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/goals', GoalViewSet, 'goals')
router.register('api/history', HistoryViewSet, 'history')

urlpatterns = router.urls