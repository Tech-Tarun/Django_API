"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import ShoppingCart, CC_Embosser, CC_Embosser_fe
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from . import views

urlpatterns = [
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('admin_log', views.admin_log, name='admin_log'), #for whole api respone on front-end
    path('customer_log', views.customer_log, name='customer_log'),
    path('cus_get/<name>/<card>', views.cus_get, name='cus_get'),
    path('cc-embosser/', CC_Embosser.as_view()),  #get_post_backend #fe_api_response
    path('', CC_Embosser_fe.as_view()), #homepage
    path('api_post', CC_Embosser_fe.as_view(),), #fe_post
]
