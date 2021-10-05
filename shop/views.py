from django.shortcuts import render
from .models import Item, ItemForm

def index(request):
    items = Item.objects.all()
    context = { 'inventory': items }
    return render(request, 'shop/index.html', context)
def add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        form.save()
    else:
        form = ItemForm()
    return render(request, 'shop/add.html', {'form':form})
    