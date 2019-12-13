from django.urls import path

from second_app import views

urlpatterns = [

    path('',views.index1,name='index1')

]