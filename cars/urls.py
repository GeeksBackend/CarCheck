from django.urls import path

from .views import index_veiw 

urlpatterns = [
    path("", index_veiw, name="index-view"),
#     path("result/", ResultView.as_view(), name="result-view"),
 ]
