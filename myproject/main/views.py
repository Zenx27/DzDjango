from django.shortcuts import render, redirect
from .forms import BookForm, IceCreamForm

def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_book')
    return render(request, 'form_book.html', {'form': form})


def create_icecream(request):
    form = IceCreamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_icecream')
    return render(request, 'create_icecream.html', {'form': form})
