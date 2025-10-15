from django.db import models
from django.contrib.auth.models import AbstractUser

class Arzt(AbstractUser):
    fachrichtung = models.CharField(max_length=100, blank=True)
    berufserfahrung = models.CharField(max_length=100, blank=True)
    nachname = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.fachrichtung})"


class Patient(models.Model):
    login = models.CharField(max_length=100, unique=True)
    benachrichtigung_wiederherstellung = models.BooleanField(default=False)
    alter = models.IntegerField()
    adhs_stadium = models.CharField(max_length=50)
    arzt = models.ForeignKey(
        Arzt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patienten'
    )

    def __str__(self):
        return f"{self.login} ({self.arzt.get_full_name() if self.arzt else '-'})"

class Gruppen(models.Model):
    name = models.CharField(max_length=100, unique=True)
    arzt = models.ForeignKey(Arzt, on_delete=models.SET_NULL, null=True, blank=True, related_name='gruppen')

    @property
    def doctor_last_name(self):
        return self.arzt.nachname if self.arzt else "-"

    def __str__(self):
        return f"{self.name} ({self.arzt})"

