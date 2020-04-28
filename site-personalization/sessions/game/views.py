from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Game, Player, PlayerGameInfo
from .forms import GameForm, GuessForm


def show_home(request):
    request.session['start'] = 'start'  # это сделано для присвоения sessionid, иначе не во всех браузерах это проиходит

    started_game_set = PlayerGameInfo.objects.filter(finished=False)  # Получаем кверисет незаверщенных игр
    current_session_id = request.COOKIES.get('sessionid')  # Идентифицируем пользователя по браузеру

    tries = 'не назначено'  # чтобы не передавать пустые здачения в context
    form = 'форма не назначена'  # чтобы не передавать пустые здачения в context
    creator = False  # чтобы не передавать пустые здачения в context
    message = ''  # чтобы не передавать пустые здачения в context

    # Если есть начатая игра
    if started_game_set:
        started_game = started_game_set[0]
        current_game_creator = started_game.player.player_session
        status = "Есть начатая игра"

        # Если текущий пользователь - создатель игры
        if current_session_id == current_game_creator:
            tries = started_game.trynumber
            creator = True

        # Если текущий пользователь - тот кто будет угадывать
        else:
            creator = False
            tries = started_game.trynumber

            # Проверяем угадано ли число:
            if started_game.game.aim == started_game.currenttry:
                message = 'Вы угадали загаданное число! \nОбновите страницу.'
                started_game.finished = True
                started_game.save()
                form = ' '

            else:

                if started_game.game.aim > started_game.currenttry:
                    message = 'Введенное число меньше угадываемого'
                    started_game.trynumber += 1

                elif started_game.game.aim < started_game.currenttry:
                    message = 'Введенное число больше угадываемого'
                    started_game.trynumber += 1

                # Обработка формы угадывания числа
                if request.method == 'POST':
                    form = GuessForm(request.POST, instance=started_game)
                    if form.is_valid():
                        form.save()

                    return redirect(reverse(show_home))

                else:
                    form = GuessForm

    # Если нет начатой игры
    else:
        status = "Надо создать игру"

        if request.method == 'POST':
            game = Game.objects.create()
            player = Player.objects.create(player_session=current_session_id)
            game.creator.add(player)

            form = GameForm(request.POST, instance=game)

            if form.is_valid():
                form.save()

            return redirect(reverse(show_home))

        else:
            form = GameForm

    context = {'forms': form,
               'status': status,
               'tries': tries,
               'started_game_set': started_game_set,
               'creator': creator,
               'message': message
               }

    return render(request, 'home.html', context)
