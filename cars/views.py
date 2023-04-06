from django.shortcuts import render
from django.views import generic
from .models import Car

# class IndexView(generic.ListView):
    # context_object_name = 'index'
    # template_name = 'index.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
        # context = super().get_context_data(**kwargs)

        # context["title"] = "Главная страница"

        # return context

def index_view(request):
    context = {"context" : "text"}
    return render(request, "cars/index.html", context=context)

# def result_view(request):
#     return render(request, "cars/result.html", context=None)
class ResultView(generic.ListView):
    queryset=Car.objects.filter(status=True)
    context_object_name = 'cars'
    template_name = 'cars/result.html'
