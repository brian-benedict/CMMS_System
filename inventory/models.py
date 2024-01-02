# from django.db import models

# # Create your models here.

# class SparePart(models.Model):
#     part_name = models.CharField(max_length=255)
#     part_description = models.TextField()
#     quantity_on_hand = models.PositiveIntegerField()
#     reorder_point = models.PositiveIntegerField()
#     vendor = models.CharField(max_length=255)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)



from django.db import models

class SparePart(models.Model):
    part_name = models.CharField(max_length=255)
    part_description = models.TextField()
    quantity_on_hand = models.PositiveIntegerField()
    reorder_point = models.PositiveIntegerField()
    vendor = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_name
