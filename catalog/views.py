from django.shortcuts import render


def index(request):
    return render(request, "catalog/index.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя - {name}\n'
              f'Телефон - {phone}\n'
              f'Сообщение - {message}\n')

    return render(request, "catalog/contact.html")
