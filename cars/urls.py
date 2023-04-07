from django.urls import path

from .views import IndexView, ResultView

urlpatterns = [
    path("", IndexView.as_view(), name="index-view"),
    path("result/<int:pk>/", ResultView.as_view(), name="result-view"),
]
