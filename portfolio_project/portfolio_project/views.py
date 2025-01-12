from django.shortcuts import render, redirect, get_object_or_404


#Helper Function for category button
def category_press(request):

    context = {}
    context['class_proj_button']    = "none"
    context['IT_proj_button']       = "none"    
    context['personal_proj_button'] = "none"
    context['cad_proj_button']      = "none"

    context['category_button'] = "inline-block"
    context['sidebar_display'] = "none"
    context['sidebar_width']   = "0%"
    context['main_left']       = "10%" 
    
    if  request.method == 'POST' and 'category-tab' in request.POST:
        context['category_button'] = "inline-block"
        context['sidebar_display'] = "block"
        context['sidebar_width']   = "25%"
        context['main_left']       = "35%" 



    if  request.method == 'POST' and 'class_proj_button' in request.POST:
        context['class_proj_button'] = "block"
        context['category_button'] = "inline-block"
        context['sidebar_display'] = "block"
        context['sidebar_width']   = "25%"
        context['main_left']       = "35%" 

    if  request.method == 'POST' and 'IT_proj_button' in request.POST:
        context['IT_proj_button'] = "block"
        context['category_button'] = "inline-block"
        context['sidebar_display'] = "block"
        context['sidebar_width']   = "25%"
        context['main_left']       = "35%"

    if  request.method == 'POST' and 'personal_proj_button' in request.POST:
        context['personal_proj_button'] = "block"
        context['category_button'] = "inline-block"
        context['sidebar_display'] = "block"
        context['sidebar_width']   = "25%"
        context['main_left']       = "35%" 
               
    if  request.method == 'POST' and 'cad_proj_button' in request.POST:
        context['cad_proj_button'] = "block"
        context['category_button'] = "inline-block"
        context['sidebar_display'] = "block"
        context['sidebar_width']   = "25%"
        context['main_left']       = "35%"        

        #context['cdisplay'] = "none"
    # if  request.method == 'POST' and 'close' in request.POST:
    #     context['category_button'] = "inline-block"
    #     context['sidebar_display'] = "none"
    #     context['sidebar_width']   = "0%"
    #     context['main_left']       = "10%" 
    return context
  
def main_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/main.html',context)

def resume_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/resume_page.html',context)

def contact_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/contact_info.html',context)

'''
Functions that list the project information
'''
# 3. Main
def class_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/class_project_page.html',context)

#3.1 ECE Capstone
def ece_capstone_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/ece_capstone.html',context)

#3.2 Web Apps
def web_apps_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/web_apps_page.html',context)

#4. Main
def it_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/it_project_page.html',context)

# 4.1 ODOO
def odoo_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/odoo_page.html',context)

#4.2 Key Tracking 
def key_tracking_action(request):
    context = category_press(request)
    return render(request, 'portfolio_project/key_tracking_page.html', context)

#4.3 Amdibd 
def amdibd_action(request):
    context = category_press(request)
    return render(request, 'portfolio_project/amdibd_page.html', context)

def personal_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/personal_project_page.html',context)

def cad_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/cad_project_page.html',context)

def ece_cad_action(request):
    context = category_press(request)
    return render(request,'portfolio_project/ece_cad.html',context)
