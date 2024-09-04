"""
URL configuration for lorax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myappmotor.views import motor_plot_view, button_page  # Import the view function

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', button_page, name='home'),  # Root URL maps to button_page view
    # path('motor-plot/', motor_plot_view, name='motor_plot'),
    # path('motor-plot/', include('myappmotor.urls')),  # Ensure this is includedß
    path('admin/', admin.site.urls),
    path('', include('myappmotor.urls')),  # This should include the URLs from your app
    path('api/', include('orderqueue.urls')),
]
