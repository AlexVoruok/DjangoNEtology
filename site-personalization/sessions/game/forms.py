from django import forms
from .models import Game, PlayerGameInfo


class GameForm(forms.ModelForm):

    aim = forms.IntegerField(max_value=10, min_value=1, label='Загадайте число от 1 до 10')

    class Meta:
        model = Game
        fields = ['aim', ]


class GuessForm(forms.ModelForm):

    currenttry = forms.IntegerField(label='Угадайте число от 1 до 10')

    class Meta:
        model = PlayerGameInfo
        fields = ['currenttry', ]
