# Mapping the views in orderqueue/views.py to the URLs

from django.urls import path
from .views import AddAndProcessOrderView, GetAllMachinesView

urlpatterns = [
    path('add-and-process-order/', AddAndProcessOrderView.as_view(), name='add-and-process-order'),
    path('get-all-machines/', GetAllMachinesView.as_view(), name='get-all-machines'),
]