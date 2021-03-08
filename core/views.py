from django.shortcuts import render

# Create your views here.
bboard = [
    [
        {'create_data': '02.01.2021'},
        {'title': 'Дом'},
        {'content': 'Дом из кирпича. 2 этажа.'},
        {'price': 3000000}
    ],
    [
        {'create_data': '24.01.2021'},
        {'title': 'Ваз 2101'},
        {'content': 'На ходу. Хорошее состояние. Почти не ездили.'},
        {'price': 32000}
    ],
    [
        {'create_data': '15.02.2021'},
        {'title': 'Квартира'},
        {'content': '2 комнаты. 3 этаж. Заезжай и живи.'},
        {'price': 12000000}
    ],
    [
        {'create_data': '18.02.2021'},
        {'title': 'Телевизор'},
        {'content': 'Диагональ 55. HDR огонь. Почти не включали.'},
        {'price': 94000}
    ],
]


def index(request):
    return render(request, 'index.html', {'data': bboard})
