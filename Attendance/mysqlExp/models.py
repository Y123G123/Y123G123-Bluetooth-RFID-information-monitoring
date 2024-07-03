from django.db import models

class BluetoothData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50)
# from django.db import models

# class Employee(models.Model):
#     card_number = models.CharField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)

# class BluetoothData(models.Model):
#     timestamp = models.DateTimeField(auto_now_add=True)
#     card_number = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=50)
