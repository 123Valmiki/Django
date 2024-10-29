#Topic DjangoSignals
#Question1

from django.core.signals import request_finished
from django.dispatch import receiver
import time

@receiver(request_finished)
def my_handler(sender, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished.")

print("Sending signal.")
request_finished.send(sender=None)
print("Signal sent.")


#Question2

from django.core.signals import request_finished
from django.dispatch import receiver
import threading

@receiver(request_finished)
def my_handler(sender, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

print(f"Main thread: {threading.current_thread().name}")
request_finished.send(sender=None)


#Question3

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Inside signal handler")
    print("Transaction state:", transaction.get_connection().in_atomic_block)

def create_object():
    with transaction.atomic():
        print("Inside transaction")
        obj = MyModel.objects.create(name="Test")
        print("Object created")

create_object()

