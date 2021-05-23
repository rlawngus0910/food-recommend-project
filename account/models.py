from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100)
    birth = models.DateTimeField()
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = "accounts"