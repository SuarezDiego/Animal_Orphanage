from django.db import models
from .person import Person


class Animal(models.Model):
    """
    Attributes:
        name: str
            Name of the animal
        description: str
            Phisical and behavioral description of the animal
        picture_url: str
            URL of a photo of the animal
        date_found: Date
            Date when the animal was found
        place_found: str
            Place where the animal was found
        date_adoption: Date
            Date of adoption of the animal
        owner: Person
            The owner of the animal
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    picture_url = models.CharField(max_length=500)
    date_found = models.DateField()
    place_found = models.CharField(max_length=500)
    date_adoption = models.DateField(null=True)
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
