from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from puddle.item.forms import NewItemForm
from .models import Item

@login_required
def details(request,pk):
    item= get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[0:4]
# Create your views here.
    return render(request, 'item/details.html', {
        'item': item,
        'related_items': related_items
        })
@login_required
def NewItem(request):
    form= NewItemForm()
    return render(request, 'item/form.html', {'form': form})