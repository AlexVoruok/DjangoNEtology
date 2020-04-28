from django.contrib import admin
from .models import Game, Player


class GameAdmin(admin.ModelAdmin):
    fields = ['aim', ]


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
