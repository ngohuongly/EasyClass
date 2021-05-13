from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Thanks',views.Thanks, name='Thanks' ),
    path('submission', views.submission, name='submission')
]
