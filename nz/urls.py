from nz.views import *
from django.urls import path
app_name='williamson'
urlpatterns=[
    path('williamson/',williamson,name='williamson'),
    path('philips/',philips,name='philips'),
]