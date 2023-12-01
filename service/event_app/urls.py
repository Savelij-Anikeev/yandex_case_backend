from rest_framework import routers

from .views import EventAPIView, UserEventRelationsAPIView

router = routers.SimpleRouter()
router.register('events', EventAPIView)
router.register('user-event-rel', UserEventRelationsAPIView)


urlpatterns = [
]

urlpatterns += router.urls
