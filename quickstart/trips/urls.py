from django.urls import path

from . import views

app_name = 'trips'
urlpatterns = [
    path('', views.index, name='index'),
    path('from/graham-conselyea', views.GrahamConselyeaView.as_view(), name='graham-conselyea'),
]