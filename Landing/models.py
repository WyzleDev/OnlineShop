from django.db import models


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    contact_number = models.CharField(max_length=128, default=None)
    password = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_zip = models.CharField(max_length=128)

    def __str__(self):
        return "[%s]%s" % (self.id, self.name)

