from django.db import models


class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product_category


# o1 = Order(
# product_category='Books',
# payment_method='Credit Card',
# shipping_cost=39,
# unit_price=59
# )
# o1.save()