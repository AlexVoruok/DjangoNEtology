from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    csv_path = settings.BUS_STATION_CSV
    with open(csv_path, encoding='cp1251') as f:
        reader = csv.DictReader(f)
        bus_station_list = []
        for row in reader:
            bus_station_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    pages = Paginator(bus_station_list, 10)

    current_num = request.GET.get('page', 1)
    current_page = pages.page(current_num)

    prev_page_url,next_page_url = None, None

    if current_page.has_previous():
        prev_p = current_page.previous_page_number()
        prev_page_url = f'bus_stations?page={prev_p}'

    if current_page.has_next():
        next_p = current_page.next_page_number()
        next_page_url = f'bus_stations?page={next_p}'

    return render_to_response('index.html', context={
        'bus_stations': current_page.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
