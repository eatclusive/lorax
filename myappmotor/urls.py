# myappmotor/urls.py
from django.urls import path, include
from .views import motor_plot_view, publish_message, subscribe_topic
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, SensorViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'sensors', SensorViewSet)

urlpatterns = [
    path('motor-plot/', motor_plot_view, name='motor_plot'),
    path('publish/', publish_message, name='publish_message'),
    path('subscribe/', subscribe_topic, name='subscribe_topic'),
    # path('', include(router.urls)),
]
