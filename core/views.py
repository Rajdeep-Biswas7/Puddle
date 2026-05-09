from django.shortcuts import render
from item.models import Item, Category
from .forms import SignUpForm
def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories,
        })

def contact(request):
    return render(request, 'core/contact.html')
# Create your views here.
def signup(request):
    form = SignUpForm()
    return render(request, 'core/signup.html', {
        'form': form
    })