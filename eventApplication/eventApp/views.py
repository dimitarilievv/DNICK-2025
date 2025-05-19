from django.shortcuts import render

from eventApp.forms import EventForm
from eventApp.models import Event, Band, EventBand
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Show events in the past
    events = Event.objects.all()
    context = {'events_list': events, 'app_name': 'eventsApp'}
    return render(request, 'index.html', context)

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event=form.save()

            bands_raw = form.cleaned_data['bands']
            band_names = [name.strip() for name in bands_raw.split(',') if name.strip()]

            for name in band_names:
                band, created = Band.objects.get_or_create(name=name)
                EventBand.objects.create(event=event, band=band)

        return redirect('index')
    else:
        form = EventForm()

    return render(request, "add_event.html", context={'form': form})
