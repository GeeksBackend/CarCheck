from django.shortcuts import render
from django.views import generic
from .models import Car

class IndexView(generic.ListView):
    model = Car
    context_object_name = 'car'
    template_name = 'cars/index.html'
    extra_context = {
        'title':'главная страница'
    }



# def result_view(request):
#     cars = Car.objects.all()
#     context = {
#         'context': 'text',
#         'cars' : cars
#     }
#     return render(request, "cars/result.html", context=context)
class ResultView(generic.DeleteView):
    model = Car
    context_object_name = 'cars'
    template_name = 'cars/result.html'


