from django.db import models
from django.forms import ModelForm

class Item(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return 'Item: {}'.format(self.name)
        
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['quantity','price','category','name','description']