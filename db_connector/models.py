from django.db import models

# Представление таблицы пользователей
class User(models.Model):
    full_name = models.CharField(max_length=300, primary_key=True) # Полное имя пользователя
    login = models.CharField(max_length=200, unique=True) # Логин пользователя
    password = models.CharField(max_length=64) # Пароль пользователя

class Client(models.Model):
    account_number = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    tin = models.CharField(max_length=12)
    responsible_user = models.ForeignKey("User", on_delete=models.CASCADE)
    status = models.CharField(null=False, default="Не в работе", max_length=50)
