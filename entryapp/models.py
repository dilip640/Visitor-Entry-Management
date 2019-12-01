from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.

class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phone_number = PhoneNumberField()

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phone_number = PhoneNumberField()
    check_in = models.TimeField(auto_now_add=True)

class PastVisitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phone_number = PhoneNumberField()
    check_in = models.TimeField(blank=False)
    check_out = models.TimeField(auto_now_add=True)

@receiver(pre_delete, sender=Visitor, dispatch_uid='visitor_delete_signal')
def visitor_deleted(sender, instance, using, **kwargs):
    PastVisitor(name=instance.name, email=instance.email,
                    phone_number=instance.phone_number, check_in=instance.check_in)