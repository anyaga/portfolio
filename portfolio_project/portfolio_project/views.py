from django.shortcuts import render, redirect, get_object_or_404


def category_press(request):
    context = {}
    context['bdisplay'] = "none"
    
    if  request.method == 'POST' and 'category-tab' in request.POST:
        context['bdisplay'] = "block"
    if  request.method == 'POST' and 'close' in request.POST:
        context['bdisplay'] = "none"
        
    return context
  


def main_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/main.html',context)


def contact_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/contact_info.html',{})

'''
Functions that list the project information
'''

def class_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/class_project_page.html',{})

def it_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/it_project_page.html',{})

def personal_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/personal_project_page.html',{})

def cad_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/cad_project_page.html',{})

