from django.shortcuts import render
from .models import Guest, Timer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Для отсчета времени
from django.utils import timezone


def invitation_guest(request, slug):
    timer = Timer.objects.first()
    # Таймер до события
    if timer:
        date_time = timer.date - timezone.now()
        days = date_time.days
        time_remaining = date_time.seconds
        hours = time_remaining // 3600
        minutes = (time_remaining % 3600) // 60
        seconds = time_remaining % 60

    model_guest = get_object_or_404(Guest, name_slug=slug)

    if request.method == "POST":
        name = request.POST['name']
        presence = request.POST['presence']
        drinks = request.POST.values()
        if 'one_plus' in request.POST:
            one_plus = request.POST['one_plus']
            model_guest.one_plus = one_plus
            model_guest.drinks = ','.join(list(drinks)[4:])
        else:
            model_guest.drinks = ','.join(list(drinks)[3:])
        model_guest.presence_on_wedding = presence
        model_guest.first_seconds_names = name
        model_guest.save()
    context = {
        'guests': model_guest,
        'days': days if timer else 0,
        'hours': hours if timer else 0,
        'minutes': minutes if timer else 0,
        'seconds': seconds if timer else 0,
    }

    return render(request, 'invitation/invitation.html', context)


def my_custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)
