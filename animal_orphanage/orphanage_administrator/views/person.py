from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView
)
from orphanage_administrator.models import Person
from orphanage_administrator.forms.person import PersonForm
from django.urls import reverse


class PersonListView(ListView):
    model = Person
    context_object_name = "persons"
    template_name = "list_of_persons.html"


class PersonCreateView(CreateView):
    form_class = PersonForm
    template_name = "add_person.html"

    def get_success_url(self):
        return reverse('person_detail', kwargs={'pk': self.object.pk})


class PersonDetailView(DetailView):
    context_object_name = "person"
    queryset = Person.objects.all()
    template_name = "detail_person.html"


class PersonDeleteView(DeleteView):
    model = Person
    template_name = "delete_person.html"
    success_url = "/persons/"


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "add_person.html"

    def get_success_url(self):
        return reverse('person_detail', kwargs={'pk': self.object.pk})
