from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


bus_station_lib = list()
with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bus_station_lib.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(bus_station_lib, 10)
    page = paginator.get_page(page_num)
    context = {
        # 'bus_stations': bus_station_lib,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
