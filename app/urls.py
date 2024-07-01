from django.urls import path
from .views import index,Measurement_optical_equipment,Optical_Glasses,optical_instruments,crystal,AboutUs,Contact


urlpatterns = [
    path('',index, name='index'),
    path('Measurement_optical_equipment/',Measurement_optical_equipment,name='Measurement_optical_equipment'),
    path('Optical_Glasses/',Optical_Glasses,name='Optical_Glasses'),
    path('optical_instruments/',optical_instruments,name='optical_instruments'),
    path('crystal/',crystal,name='crystal'),
    path('about_us/',AboutUs,name='about_us'),
    path('Contact/',Contact,name='Contact')
]
