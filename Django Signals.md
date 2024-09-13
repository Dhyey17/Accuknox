**Question 1:** By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
- **Django Signals are executed synchronously**
``` 
import time 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    print("Signal handler started...")
    time.sleep(5) 
    print("Signal handler finished.")

user = User.objects.create(username='test_user')
print("User created.") 
```

</br>

**Question 2:** Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
- **Yes**
```
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    print("Signal handler thread ID:", threading.get_ident())

print("Caller thread ID:", threading.get_ident())
user = User.objects.create(username='test_user')
```

</br>

**Question 3:** By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
- **Yes**
```
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO test_table (value) VALUES ('Signal triggered')")

try:
    with transaction.atomic():
        user = User.objects.create(username='test_user')
        raise Exception("Force rollback")
except Exception as e:
    print(e)
```
