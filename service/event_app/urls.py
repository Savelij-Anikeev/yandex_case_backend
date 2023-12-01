from django.urls import path
from rest_framework import routers

from .views import (EventAPIView, UserEventRelationsAPIView, CategoryAPIView, 
                    EventCategoryRelationsAPIView, SetUserGroup, GroupListAPIView)

router = routers.SimpleRouter()
router.register('events', EventAPIView)
router.register('user-event-rel', UserEventRelationsAPIView)
router.register('categories', CategoryAPIView)
router.register('event-category-rel', EventCategoryRelationsAPIView)


urlpatterns = [
    path('groups/', GroupListAPIView.as_view()),
    path('groups/user/<int:pk>/', SetUserGroup.as_view()),

]

urlpatterns += router.urls
