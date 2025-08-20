from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=160)
    country = models.CharField(max_length=100, null=True, blank=True)
    founded_year = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Kit(models.Model):
    KIT_TYPES = [
        ("home", "Home"),
        ("away", "Away"),
        ("third", "Third"),
        ("special", "Special"),
        ("training", "Training"),
        ("keeper", "Keeper"),
    ]
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    kit_type = models.CharField(max_length=20, choices=KIT_TYPES)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.team.name} - {self.title}"
