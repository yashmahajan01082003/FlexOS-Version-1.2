"""
URL configuration for virtualOs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('openDesktopD/<str:fName>', views.openDesktopD , name='openDesktopD'),
    path('openParti', views.openParti, name='openParti'),
    path('BSIcons/<str:fName>', views.BSIcons, name='BSIcons'),
    path('openPartiSpec/<str:fName>', views.openPartiSpec, name='openPartiSpec'),
    path('openPartiSpec2/<str:fName0>/<str:fName1>/', views.openPartiSpec2, name='openPartiSpec2'),
    path('newD', views.newD, name='newD'),
    path('newD2/<str:fName0>/', views.newD2, name='newD2'),
    path('activateVM', views.activateVM, name='activateVM'),
    path('activateRM', views.activateRM, name='activateRM'),
    path('execHand', views.execHand, name='execHand'),
    path('execHandTab', views.execHandTab, name='execHandTab'),
    path('pres', views.pres, name='pres'),
    path('execPresentation/<str:Fname>/',views.execPresentation,name='execPresentation'),
    path('assis', views.frontEndForJarvis, name='assis'),
    path('runJarvis', views.runJarvis, name='runJarvis'),
    path('terminal', views.terminal, name='terminal'),
    path('execBrightnessControl', views.execBrightnessControl, name='execBrightnessControl'),
    path('execFaceDistance', views.execFaceDistance, name='execFaceDistance'),
    path('execFaceMesh', views.execFaceMesh, name='execFaceMesh'),
    path('execVirtualVolumeController', views.execVirtualVolumeController, name='execVirtualVolumeController'),
    path('speciallyabled', views.speciallyabled, name='speciallyabled'),
    path('speciallyabled2', views.speciallyabled2, name='speciallyabled2'),
    path('drivingguide/<str:path>/', views.drivingguide, name='drivingguide'),
    path('execPresentation2/<str:Fname>/', views.execPresentation2, name='execPresentation2'),
    path('voiceGuide', views.voiceGuide, name='voiceGuide'),
    path('index3', views.index3, name='index3'),
    path('execVZoomer/<str:Fname>/', views.execVZoomer, name='execVZoomer'),
    path('faceBlur', views.faceBlur, name='faceBlur'),
    path('sarthi', views.sarthi, name='sarthi'),
    path('voiceQuery/<str:flag>/', views.voiceQuery, name='voiceQuery'),
    path('knownBook', views.knownBook, name='knownBook'),
    path('storeDet', views.storeDet, name='storeDet'),
    path('detection', views.detection, name='detection'),
    path('detection2', views.detection2, name='detection2'),
    path('pdf_reader', views.pdf_reader, name='pdf_reader'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
