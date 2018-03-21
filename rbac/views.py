from django.shortcuts import render,HttpResponse
from utils.From_utils import *
from .service.init_permission import build_menu_tree
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rbac import models
from utils.menu import build_menu_tree


@csrf_exempt
def menu(request):
    menu=build_menu_tree(request)
    return render(request, 'menu.html', locals())
    #return HttpResponse(json.dumps(menu_li))






# @csrf_exempt
# def menu(request):
#     response = {'status': True, 'data': None, 'msg': None}
#     email=request.session['email']
#     user_obj =models.UserInfo.objects.filter(email=email).first()
#     permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
#                                           'permissions__menu_id').distinct()
#     ##
#     menu=[]
#     for item in permission_item_list:
#         menu_obj=models.Menu.objects.filter(id=item['permissions__menu_id'])
#         parent=menu_obj.values('parent__caption','caption').first()
#         parent.update(item)
#         menu.append(parent)
#     response['msg']=menu
#     print(menu)
#     return HttpResponse(json.dumps(response))
#     #return  render(request,'menu.html',locals())


def add_menu(request):
    menu = build_menu_tree()
    if request.method == "GET":
        Menu_form = MenuForm()
        return render(request, 'add_menu.html', locals())
    else:
        response = {'status': True, 'data': None, 'msg': None}
        print(request.POST)
        Menu_form = MenuForm(data=request.POST)
        if Menu_form.is_valid():
            obj = models.Menu.objects.create(**Menu_form.cleaned_data)
                # 数据库中添加一条数据
                # return redirect('/login.html') # ajax跳转，错错错
        else:
            response['status'] = False
            response['msg'] = Menu_form.errors
        return HttpResponse(json.dumps(response))


def add_first_menu(request):
    menu = build_menu_tree()
    if request.method == "GET":
        Menu_form = MenuForm()
        return render(request, 'add_first_menu.html', locals())
    else:
        response = {'status': True, 'data': None, 'msg': None}
        print(request.POST)
        Menu_form = MenuForm(data=request.POST)
        if Menu_form.is_valid():
            obj = models.Menu.objects.create(**Menu_form.cleaned_data)
                # 数据库中添加一条数据
                # return redirect('/login.html') # ajax跳转，错错错
        else:
            response['status'] = False
            response['msg'] = Menu_form.errors
        return HttpResponse(json.dumps(response))



@csrf_exempt
def del_menu(request):
        response = {'status': True, 'data': None, 'msg': None}
        try:
            id=request.POST.get("id")
            obj = models.Menu.objects.filter(id=id).delete()
        except Exception as e:
            response['status'] = False
            response['msg'] = e

        return HttpResponse(json.dumps(response))


def show_menu(request):
    menu = build_menu_tree()
    if request.method == "GET":
        return render(request, 'show_menu.html', locals())


