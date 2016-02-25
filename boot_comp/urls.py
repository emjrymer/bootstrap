"""boot_comp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from boot_app.views import index_view, info_view, about_view, application_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="home"),
    url(r'^detailedinfo/', info_view, name="detailedinfo"),
    url(r'^aboutMe/', about_view, name="aboutMe"),
    url(r'^application_form/', application_view, name="applicationform")
]
