from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login_view),
    path('login', views.login_view),
    path('data-table', views.show_data_table),
]
