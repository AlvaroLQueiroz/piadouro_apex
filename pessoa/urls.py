from django.urls import path
from pessoa.views import Home, UserList, Follow, RedirectHome

urlpatterns = [
    path('', RedirectHome.as_view(), name='home'),
    path('usuarios/', UserList.as_view(), name='usuarios'),
    path('follow/<int:profile_id>', Follow.as_view(), name='follow'),
    path('<username>/', Home.as_view(), name='perfil'),
]
