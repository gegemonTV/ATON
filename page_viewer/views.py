from django.shortcuts import render, redirect
from db_connector import models as db

# Create your views here.
def redirect_to_login_view(request):
    return render(request, 'home_page/index.html')

def login_view(request):
    return render(request, 'login_page/index.html')

def show_data_table(request):
    if request.method == "GET":
        return render(request, 'data_table/index.html')


