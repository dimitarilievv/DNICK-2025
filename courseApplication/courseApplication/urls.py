"""
URL configuration for courseApplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from courseApp import views as courseAppViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',courseAppViews.index,name='index'),
    path('add_course/',courseAppViews.add_course,name='add_course'),
    path('edit_course/<int:course_id>/', courseAppViews.add_course, name = 'edit_course')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
