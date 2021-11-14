from django.urls import include, path
from rest_framework import routers
from .views import ScheduleViewSet, CreateScheduleViewSet

router = routers.SimpleRouter()
router.register(r'update_db', CreateScheduleViewSet)
router.register(r'schedule', ScheduleViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]