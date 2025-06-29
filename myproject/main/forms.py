from django import forms
from .models import Book, IceCream


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price'] 

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = '__all__'
        widgets = {
            'flavor': forms.TextInput(attrs={'placeholder': 'Вкус'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
