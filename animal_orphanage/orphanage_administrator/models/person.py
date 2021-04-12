from django.db import models


class Person(models.Model):
    """
    Attributes:
        name: str
            Name of the person
        rut: str
            National identification number of the person
        mistreats_animals: Boolean
            Indicates if the person mistreats animals
    """

    name = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    mistreats_animals = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.rut