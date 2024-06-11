from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexAPIView.as_view()),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('aktyorlar/<int:pk>/tahrirlash/', AktyorTahrirlashAPIView.as_view()),
    path('aktyorlar/<int:pk>/', AktyorDetailAPIView.as_view()),
    path('aktyorlar/<int:pk>/delet/', AktyordeleteAPIView.as_view()),
    path('tariflar/', TariflarAPIView.as_view()),
    path('tariflar/<int:pk>/', TarifDetailAPIView.as_view()),
    path('tariflar/<int:pk>/delet/', TarifdeleteAPIView.as_view()),
    path('tariflar/<int:pk>/tahrirlash/', TarifTahrirlashAPIView.as_view()),
]
