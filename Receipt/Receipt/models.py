import uuid

from django.db import models

class Receipt(models.Model):
    receipt_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField(default='2023-01-01')  # Provide a default date value
    standard = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    enrollment_no = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
    received = models.CharField(max_length=50, choices=[
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('card', 'Card'),
    ])
    status = models.CharField(max_length=50, choices=[
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ])
    signature = models.CharField(max_length=100)


    def __str__(self):
        return self.name
