
from django.urls import path
from . import views

#app_name='schoolcalendar'
urlpatterns=[
#    path('', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/', views.event, name='event_new'),

]
#from django.conf.urls import url
#from . import views

#app_name = 'Schoolcalendar'
#urlpatterns = [
#    url(r'^index/$', views.index, name='index'),
#    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
#]
