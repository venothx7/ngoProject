from django.db import models
from event.models import Event


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    adult_qty = models.PositiveIntegerField()
    child_qty=models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
       return sum(item.get_cost() for item in self.items.all())


class Registration(models.Model):
    registration = models.ForeignKey(Register, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2)
    child_price = models.DecimalField(max_digits=10, decimal_places=2)
    adult_quantity = models.PositiveIntegerField(default=1)
    child_quantity = models.PositiveIntegerField(default=0)

    def create(cls, event, adult_price, child_price, adult_quantity, child_quantity):
        registration = cls(event=event, adult_price=adult_price, child_price=child_price,
                           adult_quantity=adult_quantity, child_quantity=child_quantity)
        return registration


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.adult_price * self.adult_quantity + self.child_price * self.child_quantity
