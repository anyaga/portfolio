from django.shortcuts import render, redirect, get_object_or_404


def main_action(request):
    return render(request,'portfolio_project/main.html',{})


def contact_action(request):
    return render(request,'portfolio_project/contact_info.html',{})

'''
Functions that list the project information
'''

def class_action(request):
    return render(request,'portfolio_project/class_project_page.html',{})

def it_action(request):
    return render(request,'portfolio_project/it_project_page.html',{})

def personal_action(request):
    return render(request,'portfolio_project/personal_project_page.html',{})

