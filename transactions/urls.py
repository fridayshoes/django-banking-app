from django.urls import path
from . import views

urlpatterns = [
    # This matches: /transactions/personal/
    path('personal/', views.personal_transactions, name='personal_transactions'),

    # This matches: /transactions/business/
    path('business/', views.business_transactions, name='business_transactions'),
]