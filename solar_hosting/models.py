from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db.models import CharField


class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name="Ім'я")
    last_name = models.CharField(max_length=30, verbose_name="Прізвище")
    username = models.CharField(max_length=30, unique=True, verbose_name="Логін")
    email = models.EmailField(unique=True, verbose_name="Електронна пошта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class HostingPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    plan_id = models.CharField(max_length=20, unique=True, verbose_name="Ідентифікатор плану")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    description = models.TextField(verbose_name="Опис")
    domains = models.IntegerField(verbose_name="Домени")
    disk_space = models.IntegerField(verbose_name="Диск (МБ)")
    bandwidth = models.IntegerField(verbose_name="Трафік (МБ)")
    free_domains = models.IntegerField(verbose_name="Додаткові домени")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "План хостингу"
        verbose_name_plural = "Плани хостингу"


class HostingPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    plan = models.ForeignKey(HostingPlan, on_delete=models.CASCADE, verbose_name="План хостингу")
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата покупки")

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} ({self.purchase_date})"

    class Meta:
        verbose_name = "Покупка хостингу"
        verbose_name_plural = "Покупки хостингу"


class DomainPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    domain_name = models.CharField(max_length=255, verbose_name="Ім'я домену")
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата покупки")

    def __str__(self):
        return f"{self.user.username} - {self.domain_name} ({self.purchase_date})"

    class Meta:
        verbose_name = "Покупка домену"
        verbose_name_plural = "Покупки доменів"


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.timestamp})"

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"


