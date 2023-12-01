from rest_framework import routers

from .views import EventAPIView, UserEventRelationsAPIView, CategoryAPIView, EventCategoryRelationsAPIView

router = routers.SimpleRouter()
router.register('events', EventAPIView)
router.register('user-event-rel', UserEventRelationsAPIView)
router.register('categories', CategoryAPIView)
router.register('event-category-rel', EventCategoryRelationsAPIView)


urlpatterns = [
]

urlpatterns += router.urls
