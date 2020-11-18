from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Company(models.Model):
    name = models.CharField(
        verbose_name="会社名",
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.name;


class Item(models.Model):
    name = models.CharField(
        verbose_name="商品名",
        max_length=255,
    )
    price = models.IntegerField(
        verbose_name="金額",
        default = 0,
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.name;


class Order(models.Model):
    title = models.CharField(
        verbose_name="受注名",
        max_length=255,
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        verbose_name="会社",
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.title;


class OrderDetail(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        verbose_name="受注",
    )
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        verbose_name="商品",
    )
    unit = models.IntegerField(
        verbose_name="個数",
        default=0,
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.orer.title + ", " + self.item.name + ", " + self.unit;

