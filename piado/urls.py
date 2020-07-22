from django.urls import path
from piado.views import PiadoCreate

urlpatterns = [
    path('', PiadoCreate.as_view(), name='piado-create'),
]
