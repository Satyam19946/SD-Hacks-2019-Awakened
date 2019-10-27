from django.shortcuts import render, get_object_or_404

# Create your views here.
import numpy as np
from .models import Driver

# Get the driver details and display them
def index(request):
    latest_driver_list1 = list(Driver.objects.order_by('name_text'))
    latest_driver_list = []
    for i in latest_driver_list1:
        if i not in latest_driver_list:
            latest_driver_list.append(i)
    context = {'latest_driver_list':latest_driver_list}
    return render( request, 'driverDatabase/index.html', context )


def driverDetail( request, driver_id ):
    driver = get_object_or_404( Driver, pk=driver_id)
    a = list(Driver.objects.filter(name_text=driver.name_text))
    context = { 'thisDriversRides':a }
    return render( request, 'driverDatabase/driverDetail.html', context)
