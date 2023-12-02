from django.urls import path
from rest_framework import routers

from .views import (EventAPIView, UserEventRelationsAPIView, CategoryAPIView, 
                    EventCategoryRelationsAPIView, SetUserGroup, GroupListAPIView, VerifyEventAPIView)

router = routers.SimpleRouter()
router.register('events', EventAPIView)
router.register('user-event-rel', UserEventRelationsAPIView)
router.register('categories', CategoryAPIView)
router.register('event-category-rel', EventCategoryRelationsAPIView)


urlpatterns = []

urlpatterns += router.urls

urlpatterns += [
    path('groups/', GroupListAPIView.as_view()),
    path('groups/user/<int:pk>/', SetUserGroup.as_view()),
    path('verify/event/<int:pk>/', VerifyEventAPIView.as_view()),
]
