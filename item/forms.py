from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-300'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-300'}),
        }