from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
# Главная страница
#def index(request):    
    #return HttpResponse('Главная страница')



def index(request):
    template = 'posts/index.html'
    
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context) 


def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        # В словарь можно передать переменную
        
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context) 
    
    