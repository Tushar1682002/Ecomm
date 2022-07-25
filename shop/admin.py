from django.contrib import admin
from pandas import concat

# Register your models here.


from .models import Product
admin.site.register(Product)


from .models import Order
admin.site.register(Order)

from .models import Contact
admin.site.register(Contact)

from .models import OrderUpdate
admin.site.register(OrderUpdate)