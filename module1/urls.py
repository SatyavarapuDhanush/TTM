from django.contrib import admin
from django.urls import path
from.views import*
from.forms import *

urlpatterns = [
    path('Hello/', hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='home'),
    path('travelcard/',travelpackage,name='travelcard'),
    path('p/', print1, name='p'),
    path('print/', Print_to_console, name='print'),
    path('rand/',rand,name='rand'),
    path('ran1/',random123,name='random123'),
    path('date/',get_date,name='date'),
    path('date1/',getdate1,name='date1'),
   # path('tcall/',tzfunctioncall,name='tcall'),
   #path('tlogic',tzfunctionlogic,name='tlogic'),
   path('reg/', register1, name='register1'),
   path('reg1/', registerloginfunction, name='registerloginfunction'),
   path('pie1/',pie_chart1,name='pie1'),
   path('pie/',pie_chart,name='pie'),
   path('slides/',slides,name='slides'),
   path('weathercall/',weatherpagecall,name='weathercall'),
   path('weatherlogic/',weatherpagecall,name='weatherlogic'),
   path('signup/',signup,name='signup'),
   path('login/',login,name='login'),
   path('login1/',login1,name='login1'),
   path('signup1/',signup1,name='signup1'),
   path('logout/',logout,name='logout'),
   path('feedback/',feedback,name='feedback'),
   path('cmail/',contactmail,name='contactmail'),
]