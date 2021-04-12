from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView
)
from orphanage_administrator.models import Animal
from orphanage_administrator.forms.animal import AnimalForm, AdoptForm
from django.urls import reverse


class AnimalListView(ListView):
    model = Animal
    context_object_name = "animals"
    template_name = "list_of_animals.html"

class AnimalDetailView(DetailView):
    context_object_name = "animal"
    queryset = Animal.objects.all()
    template_name = "detail_animal.html"

class AnimalCreateView(CreateView):
    form_class = AnimalForm
    template_name = "add_dog.html"
    def get_success_url(self):
        return reverse('animal_detail', kwargs={'pk': self.object.pk})

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = "delete_animal.html"
    success_url = "/animals/"

class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = "add_dog.html"
    def get_success_url(self):
        return reverse('animal_detail', kwargs={'pk': self.object.pk})

class AdoptView(UpdateView):
    model = Animal
    form_class = AdoptForm
    template_name = "adopt.html"
    def get_success_url(self):
        return reverse('animal_detail', kwargs={'pk': self.object.pk})
