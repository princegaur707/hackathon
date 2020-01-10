from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getuserfeedbackform',views.getuserfeedbackform,name="getuserfeedbackform"),
    path('saveuserfeedbackform',views.saveuserfeedbackform,name="saveuserfeedbackform"),

]