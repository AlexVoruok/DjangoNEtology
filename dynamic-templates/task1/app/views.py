import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    inflation_list = []
    with open('inflation_russia.csv', encoding='utf8') as csvf:
        reader = csv.reader(csvf, delimiter = ';')
        for row in reader:
            line = []
            for month in row:
                # print(row)
                line.append(month)
            inflation_list.append(line)




    # чтение csv-файла и заполнение контекста
    context = {'inflation_data': inflation_list}

    return render(request, template_name,
                  context)