from django.shortcuts import render
from .models import MenuItem


def index(request):
    main_menu = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'index.html', {'main_menu': main_menu})


def menu_detail(request, menu_id):
    menu_item = MenuItem.objects.get(id=menu_id)
    children = menu_item.children.all()
    return render(request, 'menu_detail.html',
                  {'menu_item': menu_item, 'children': children, 'menu_image': menu_item.image})


def draw_menu(request, menu_id):  # Добавьте это
    menu_item = MenuItem.objects.get(id=menu_id)
    return render(request, 'draw_menu.html', {'menu_item': menu_item})
