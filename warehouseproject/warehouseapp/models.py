from django.db import models

# Create your models here.
CATEGOTY =(
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('construction', 'construction'),
    ('pharmacitical', 'pharmacitical'),
    ('clothings', 'clothings'),
    ('jewellery', 'jewellery'),
    ('sports materials','sports materials'),
    ('Furniture', 'furniture'),

)

class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGOTY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)


    @property
    def price_total(self):
        return self.quantity * self.price


    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.price}'


class Contacts(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return f'{self.username}-{self.email}-{self.message}'