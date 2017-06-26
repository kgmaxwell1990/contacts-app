from django.shortcuts import render, redirect
from .models import Contact
from .forms import NewContactForm

# Create your views here.

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        form = NewContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_contacts)
    else:
        form = NewContactForm()

    return render(request, 'add.html', {'form': form})
