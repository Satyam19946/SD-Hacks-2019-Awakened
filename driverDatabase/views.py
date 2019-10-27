from django.shortcuts import render

# Create your views here.

from .models import Driver

# Get the driver details and display them
def index(request):
    latest_driver_list = Driver.objects.order_by('-date')[:5]
    context = {'latest_driver_list':latest_driver_list}
    return render(request, 'driverDatabase/index.html', context)


def driverDetail( request, driver_id ):
    driver = get_object_or_404( Driver, pk=driver_id)
    return render( request, 'driverDatabase/driverDetail.html')
