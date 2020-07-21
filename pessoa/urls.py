from django.urls import path
from pessoa.views import Home

urlpatterns = [
    path('<username>/', Home.as_view(), name='perfil'),
]
