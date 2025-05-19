from django.shortcuts import render, redirect

from cakeApp.forms import CakeForm
from cakeApp.models import Cake


# Create your views here.
def index(request):
    # Show flights in the past
    cakes = Cake.objects.all()
    context = {'cake_list': cakes, 'app_name': 'cakeApp'}
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = CakeForm()
    return render(request, "add.html", context={'form': form})