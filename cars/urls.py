from django.urls import path

from .views import index_view, result_view

urlpatterns = [
    path("", index_view, name="index-view"),
    path("result/", result_view, name="result-view"),
]
