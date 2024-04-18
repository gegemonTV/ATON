from django.urls import path
from . import views

urlpatterns = [
    path('/request-table/', views.request_table),
    path('/set-status/', views.set_status),
]