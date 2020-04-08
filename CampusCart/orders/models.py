from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=False)
    # address = models.CharField(max_length=250)
    # postal_code = models.CharField(max_length=20)
    place_of_residence = models.CharField(max_length=50, blank=False)
    room_number = models.CharField(max_length=2 , blank=False)
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10 , blank=False)
    registration_number = models.CharField(max_length=20,blank=False)
    identification_number = models.CharField(max_length=20 , blank=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
