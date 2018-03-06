from django.db import models
from django.utils import timezone

from account.models import User

DECK_TYPE_CHOICES = (
    (0, 'None'),
    (1, 'Cycle'),
    (2, 'Spell Bait'),
    (3, 'Beatdown'),
    (4, 'Spawner'),
    (5, 'Three Crowns'),
    (6, 'Control'),
    (7, 'Siege'),
)


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    cards = models.CharField(max_length=200, blank=False, null=False)
    type = models.IntegerField(choices=DECK_TYPE_CHOICES)
    avg_elixir = models.FloatField(blank=False, null=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({DECK_TYPE_CHOICES[self.type][1]} - {self.avg_elixir})"

    class Meta:
        verbose_name = 'Deck'
        verbose_name_plural = 'Decks'
        get_latest_by = 'date_created'
        ordering = ['-date_created', ]