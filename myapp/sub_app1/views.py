from django.shortcuts import render
from django.http import HttpResponse
from .forms import GetContactForm


# Create your views here.

def get_contacts(request):

    if request.method == 'POST':
        form = GetContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)
    form = GetContactForm()
    return render(request, 'form.html', {'form': form})
