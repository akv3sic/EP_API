from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FailureViewSet

# Create a router and register the FailureViewSet with it
router = DefaultRouter()
router.register(r'failures', FailureViewSet, basename='failure')

urlpatterns = [
    # Include the URLs generated by the router
    path('', include(router.urls)),
]
