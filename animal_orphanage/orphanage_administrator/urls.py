from django.urls import path
from django.views.generic.base import RedirectView
from orphanage_administrator.views.animal import (
    AnimalListView,
    AnimalCreateView,
    AnimalDetailView,
    AnimalDeleteView,
    AnimalUpdateView,
    AdoptView
)
from orphanage_administrator.views.person import (
    PersonListView,
    PersonCreateView,
    PersonDetailView,
    PersonDeleteView,
    PersonUpdateView
)


urlpatterns = [
    path('animals/', AnimalListView.as_view(), name="list_of_animals"),
    path('add_animal/', AnimalCreateView.as_view(), name="add_animal"),
    path('add_person/', PersonCreateView.as_view(), name="add_person"),
    path('update_animal/<int:pk>/', AnimalUpdateView.as_view(), name="update_animal"),
    path('adopt/<int:pk>/', AdoptView.as_view(), name="adopt_animal"),
    path('update_person/<int:pk>/', PersonUpdateView.as_view(), name="update_person"),
    path('persons/', PersonListView.as_view(), name="list_of_persons"),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name="animal_detail"),
    path('person/<int:pk>/', PersonDetailView.as_view(), name="person_detail"),
    path('delete_animal/<int:pk>/', AnimalDeleteView.as_view(), name="delete_animal"),
    path('delete_person/<int:pk>/', PersonDeleteView.as_view(), name="delete_person"),
    path('',RedirectView.as_view(url='animals'))
]
