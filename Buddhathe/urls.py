"""Buddhathe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rbac import views as rbac_views
from cmdb import views
urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^index', views.index),
    url(r'^show_service_line', views.show_service_line),
    url(r'^add_service_line', views.add_service_line),
    url(r'^update_service_line', views.update_service_line),
    url(r'^del_service_line', views.del_service_line),
    url(r'^add_host', views.add_host),
    url(r'^del_host', views.del_host),
    url(r'^menu', rbac_views.menu),
    url(r'^add_menu', rbac_views.add_menu),
    url(r'^show_menu', rbac_views.show_menu),
    # url(r'^base', rbac_views.base),
    url(r'^add_first_menu', rbac_views.add_first_menu),
    url(r'^del_menu', rbac_views.del_menu),
    url(r'^add_app', views.add_app),

]