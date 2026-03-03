from django.urls import path
from . import views
 
urlpatterns = [
     path('enroll/', views.enroll_user, name='enroll_user'),
     path('enrolled/', views.enrolled_user, name='enrolled_user'),
 
]