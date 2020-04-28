from django.db import models


class Player(models.Model):
    player_session = models.CharField(max_length=32, default='')


class Game(models.Model):
    aim = models.IntegerField(verbose_name='Загадайте число от 1 до 10', default=0)
    creator = models.ManyToManyField(Player, through='PlayerGameInfo')


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, default='', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, default='', on_delete=models.CASCADE)
    trynumber = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)
    currenttry = models.IntegerField(default=0)

