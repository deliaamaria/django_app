from django.urls import path
from GooglePlayStoreApp import views

urlpatterns = [
    path('plot/', views.plot, name="plot"),
    path('plot1/', views.plot1, name="plot1"),
    path('plot2/', views.plot2, name="plot2"),
    path('plot3/', views.plot3, name="plot3"),
    path('plot4/', views.plot4, name="plot4"),
]