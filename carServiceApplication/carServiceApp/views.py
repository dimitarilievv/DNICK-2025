from django.shortcuts import render, redirect

from carServiceApp.forms import ServiceForm
from carServiceApp.models import Service


# Create your views here.
def index(request):
    return render(request,'index.html')

def repairs(request):
    services=Service.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('repairs')
    else:
        form = ServiceForm()

    context = {'service_list': services, 'app_name': 'carServiceApp',"form":form}

    return render(request, "repairs.html", context)