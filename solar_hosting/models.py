from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class HostingPlan(models.Model):
    name = models.CharField(max_length=100)
    plan_id = models.CharField(max_length=20, unique=True)  # Уникальный идентификатор плана
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    domains = models.IntegerField()
    disk_space = models.IntegerField()
    bandwidth = models.IntegerField()
    free_domains = models.IntegerField()

    def __str__(self):
        return self.name


class HostingPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(HostingPlan, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} ({self.purchase_date})"


class DomainPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=255)  # Имя домена
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.domain_name} ({self.purchase_date})"
