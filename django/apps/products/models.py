from django.core.validators import *
from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200, null=False, unique=True)
    ml_product = models.CharField('Ml Product', max_length=200)
    stock = models.PositiveIntegerField('Stock', default=0)
    status = models.BooleanField('Status', null=False, default=True, )
    created_at = models.DateTimeField('Created at', auto_now_add=True, null=True, editable=False, )
    updated_at = models.DateTimeField('Updated at', auto_now=True, null=True, editable=False, )

    def product_format(self):
        return "{} / {}".format(self.title, self.ml_product)

    def __str__(self):
        return self.product_format()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'
        ordering = ['id']


class User(models.Model):
    pass
