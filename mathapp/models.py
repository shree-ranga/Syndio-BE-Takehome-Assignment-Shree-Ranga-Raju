from django.db import models


class Employees(models.Model):
    protected_class = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    tenure = models.IntegerField(blank=True, null=True)
    performance = models.IntegerField(blank=True, null=True)
    compensation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # django will not create or alter the table
        db_table = "employees"
