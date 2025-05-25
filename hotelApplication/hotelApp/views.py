from django.shortcuts import render, get_object_or_404, redirect

from hotelApp.forms import ReservationForm
from hotelApp.models import Reservation, RoomEmployee


# Create your views here.
def index(request):
    reservations = Reservation.objects.filter(room__num_beds__lt=5,room__is_cleaned=True).all()
    context={'reservation_list':reservations}
    return render(request,'index.html',context)

def details(request, reservation_id):
    reservation = Reservation.objects.filter(id=reservation_id).first()
    context={'reservation_data':reservation}
    return render(request,'details.html',context)

def edit_reservation(request,reservation_id):
    reservation = get_object_or_404(Reservation,pk=reservation_id)
    if request.method == 'POST':
        form=ReservationForm(request.POST,request.FILES,instance=reservation)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = ReservationForm(instance=reservation)
    return render(request,"edit_reservation.html",context={'form':form,'reservation_id':reservation_id})