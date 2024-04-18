from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
import json
from db_connector import models as db

# Create your views here.
def request_table(request):
    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = db.User.objects.filter(login=login).first()
        if user == None or user.password != password:
            return redirect('/login?e=incorrect')
        return redirect(f'/data-table?r={user.full_name}')
    if request.method == "GET":
        responsible = request.GET.get('r')
        clients = db.Client.objects.filter(responsible_user = responsible).values('account_number', 'date_of_birth', 'first_name', 'id', 'last_name', 'middle_name', 'responsible_user', 'responsible_user_id', 'status', 'tin')
        serialized = json.dumps(list(clients), cls=DjangoJSONEncoder)
        return JsonResponse({'data': serialized})

@csrf_exempt
def set_status(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        status = request.POST.get('status')
        client = db.Client.objects.filter(first_name=first_name, last_name=last_name, middle_name=middle_name).first()
        client.status = status
        client.save()
        return HttpResponse("ok")