from django.db import models

# Creating the customer class
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    microgreen_type = models.CharField(max_length=255)
    microgreen_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimatedTime = models.DurationField()

    def __str__(self):
        return f"{self.customer_name} - {self.microgreen_type}"

