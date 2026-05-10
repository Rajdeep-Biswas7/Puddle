from django.shortcuts import render, redirect
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

# Updated signup view to handle form submissions
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })