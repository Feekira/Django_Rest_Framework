from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    age = models.IntegerField()

    # definindo meu STR
    def __str__(self):
        return self.name