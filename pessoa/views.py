from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from pessoa.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, DetailView):
    template_name = 'home.html'
    model = User

    def get_object(self):
        return get_object_or_404(self.model, username=self.kwargs['username'])


class UserList(LoginRequiredMixin, ListView):
    template_name = 'user_list.html'
    model = Perfil


class Follow(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'usuarios'

    def get_redirect_url(self, *args, **kwargs):
        profile_to_follow = get_object_or_404(Perfil, pk=kwargs['profile_id'])
        if self.request.user.perfil.seguindo.filter(pk=profile_to_follow.pk).exists():
            self.request.user.perfil.seguindo.remove(profile_to_follow)
        else:
            self.request.user.perfil.seguindo.add(profile_to_follow)
        return super().get_redirect_url()

class RedirectHome(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'perfil'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(self.request.user.username)
