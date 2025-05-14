from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def hello_world(request):
    return HttpResponse("Veriserve Django app.")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'result.html', {'name': name, 'email': email, 'message': message})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
