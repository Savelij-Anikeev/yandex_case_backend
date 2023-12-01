from rest_framework import routers

from .views import EventAPIView

router = routers.SimpleRouter()
router.register('events', EventAPIView)


urlpatterns = [
    
]
urlpatterns += router.urls