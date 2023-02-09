import django_filters
from .models import Products



class filterProducts(django_filters.FilterSet):
    class Meta :
        model = Products
        fields = ['name']