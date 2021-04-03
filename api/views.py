from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from api.models import Client, Address


class HomeListView(ListView):
    model = Client
    template_name = 'home.html'


class ClientListView(ListView):
    model = Client
    template_name = 'details.html'
    context_object_name = 'client'

    def get_queryset(self):
        return Client.objects.get(id=self.kwargs['id'])


class ClientCreate(CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'date_of_birth', 'address']
    initial = {'date_of_death': '12/10/2016', }
    template_name = 'client_form.html'
    success_url = reverse_lazy('home')


class ClientUpdate(UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'date_of_birth', 'address']
    template_name = 'client_form.html'
    success_url = reverse_lazy('home')


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('home')
    template_name = 'client_delete_confirm.html'

