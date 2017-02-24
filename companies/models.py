from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=5)
    open_share_value = models.CharField(name='open', max_length=5)
    close = models.CharField(max_length=5)
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker
