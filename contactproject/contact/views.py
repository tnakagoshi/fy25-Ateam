from django.shortcuts import render

from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

class CotactListView(ListView):
    template_name = 'contact/list.html'
    model = Contact
    