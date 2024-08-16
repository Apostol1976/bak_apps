from main.models import Catalog
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    
    catalog=Catalog.objects.all()
    
    
    context = {
        'content':'Пластиковые окна для Вашего дома',
        'catalog': catalog
    }
    
    return render(request,'main/index.html', context)


def about(request):
    
    
    
    
    context = {
        'content':'О нас',
        'text_on_the_page':'Наша компания – лидер в производстве и установке пластиковых окон на российском рынке. Наша миссия – создавать комфорт и уют в каждом доме, предлагая высококачественные, экологически чистые и энергоэффективные оконные конструкции. Мы используем передовые технологии и материалы, чтобы удовлетворить потребности самых требовательных клиентов. Мы ваш надежный партнер в создании комфортного и безопасного жилища. Мы предлагаем только лучшие решения для вашего дома, обеспечивая высокое качество, энергоэффективность и долговечность наших оконных конструкций. Обратитесь к нам, и мы сделаем ваш дом уютным и теплым!'
       
    }
    return render(request,'main/about.html', context)


def contact(request):
    context = {
        'content':'Контактная информация',
        'text_on_page':'Адрес: Латвия, г. Рига, ул. Бривибас, д. 100, офис 20',
       
    }
    return render(request,'main/contact.html', context)