from django.db import models

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    createdAt = models.DateField(
        null=False,
        blank=False,
        auto_now_add = True
    )
    lastChangeDate = models.DateTimeField(
        null=True,
        blank=False,
        auto_now = True
    )
    isActive = models.BooleanField(
        null=False,
        blank=False,
        default=True
    )

    class Meta:
        managed = True
        db_table = 'test'