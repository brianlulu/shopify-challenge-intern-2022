from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    warehouse_list = models.ManyToManyField('Warehouse', through='Inventory')

    def __str__(self):
        return self.name

class Warehouse(models.Model): 
    name = models.CharField(max_length=50)
    product_list = models.ManyToManyField(Product, through='Inventory')

    def __str__(self):
        return self.name

#TODO: quantity check: if zero quantity should not able to do negative inventory
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits = 10,decimal_places=2) # choose decimal over float bc decimal is more close to human calculation
    date_created = models.DateTimeField(auto_now_add=True)





