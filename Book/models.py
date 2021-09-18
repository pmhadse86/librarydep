from django.db import models
from django.db.models.fields import IntegerField


# id, name, qty, price, is_published, author

class Book(models.Model):
        name = models.CharField(max_length=100)
        qty = models.IntegerField()
        price = models.FloatField()
        is_published = models.BooleanField(default=False)
        published_date = models.DateField(null=True)
        is_deleted = models.CharField(max_length= 1, default= "N")

        def __str__(self):
                return f"{self.__dict__}"

        class Meta:
                db_table = "book"