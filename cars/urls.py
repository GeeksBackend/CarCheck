from django.urls import path

from .views import index_view, ResultView

urlpatterns = [
    path("", index_view, name="index-view"),
    path("result/", ResultView.as_view(), name="result-view"),
]
