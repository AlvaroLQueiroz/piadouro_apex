from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from piado.models import Piado
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

class PiadoCreate(LoginRequiredMixin, CreateView):
    model = Piado
    fields = ['conteudo']

    def form_valid(self, form):
        form.instance.usuario = self.request.user.perfil
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('perfil', args=[self.request.user.username])

class PiadoDelete(LoginRequiredMixin, DeleteView):
    model = Piado
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.usuario.usuario.id != request.request.user.id:
            raise PermissionDenied
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
