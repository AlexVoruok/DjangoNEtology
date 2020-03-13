from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    if request.GET.get('from-landing') == 'original':
        counter_click['original'] += 1
    elif request.GET.get('from-landing') == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request, ab_test_arg):
    print(ab_test_arg)
    if ab_test_arg == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')

    elif ab_test_arg == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')


def stats(request):
    try:
        test_conversion = counter_click['test']/counter_show['test']
    except ZeroDivisionError:
        test_conversion = 'нет данных'

    try:
        original_conversion = counter_click['original']/counter_show['original']
    except ZeroDivisionError:
        original_conversion = 'нет данных'

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
