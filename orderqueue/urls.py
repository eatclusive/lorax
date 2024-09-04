# Mapping the views in orderqueue/views.py to the URLs

from django.urls import path
from .views import AddOrderView, GetNextOrderView

urlpatterns = [
    path('add-order/', AddOrderView.as_view(), name='add-order'),
    path('get-next-order/', GetNextOrderView.as_view(), name='get-next-order'),
]