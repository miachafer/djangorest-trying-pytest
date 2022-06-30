from django.db import models

class Pessoa(models.Model):
    idade = models.IntegerField()

    def __str__(self):
        return self.idade