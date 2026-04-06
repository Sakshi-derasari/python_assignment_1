from django.shortcuts import render
from .models import InstituteLocation

def map_view(request):
    city = request.GET.get('city', 'Ahmedabad')
    locations = InstituteLocation.objects.filter(city__iexact=city)

    context = {
        'locations': list(locations.values()),
        'city': city
    }

    return render(request, 'location/map.html', context)