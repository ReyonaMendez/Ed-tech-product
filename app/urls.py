
from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.white),
    # path('app/<str:id>',views.result,name ='result_name')
]
