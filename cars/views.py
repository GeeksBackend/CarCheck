from django.shortcuts import render
from django.views import generic

from cars.forms import CarSearchForm
from .models import Car


def index_veiw(request):
    if request.method == 'POST':
        form = CarSearchForm(request.POST)
        if form.is_valid():
            license_plate = form.cleaned_data['license_plate']
            car = Car.objects.filter(license_plate=license_plate).first()
            return render(request, 'cars/result.html', {'car': car})
    else:
        form = CarSearchForm()
    return render(request, 'cars/index.html', {'form': form})





