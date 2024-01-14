from django_filters import rest_framework as filters

from .models import StoreUser


class StoreUserFilter(filters.FilterSet):
    store = filters.NumberFilter()

    class Meta:
        model = StoreUser
        fields = ['store', ]
