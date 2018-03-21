from django.shortcuts import render,redirect,HttpResponse
from utils.md5 import encrypt
from utils.From_utils import *
from cmdb import models
from rbac import models as rbac_modes
from rbac.service.init_permission import  build_menu_tree
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
from rbac.service.init_permission import init_permission
from django.conf import settings








def register(request):
    if request.method == "GET":
        register_form = RegisterForm()
        return render(request,'register.html',locals())
    else:
        response = {'status': True, 'data': None, 'msg': None}
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            register_data=register_form.cleaned_data
            register_data['password']=encrypt(register_data['password'])
            obj=rbac_modes.UserInfo.objects.create(**register_form.cleaned_data)
            # 数据库中添加一条数据
            # return redirect('/login.html') # ajax跳转，错错错
        else:
            response['status'] = False
            response['msg'] = register_form.errors
        return HttpResponse(json.dumps(response))


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        pwd = encrypt(pwd)
        user_obj = rbac_modes.UserInfo.objects.filter(email=email,password=pwd).first()
        if user_obj:
            # 生成随机字符串
            # cookie发送给客户端
            # 服务端随机字符串作为key, 自己设置一些values{}
            request.session['email'] = email
            init_permission(request, user_obj)
            return redirect("/index")
            # print(request.session['email'])
            # print(request.session[settings.SESSION_PERMISSION_URL_KEY])
            # print(request.session[settings.SESSION_PERMISSION_MENU_URL_KEY])

            # return HttpResponse('OK')

        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})


def index(request):
    # menu = build_menu_tree(request)
    all_host=models.host.objects.all()
    return render(request, 'index.html',locals())



def show_service_line(request):
    # menu = build_menu_tree()
    all_service_line=models.Service_Line.objects.all()
    return render(request, 'show_service_line.html',locals())



def add_service_line(request):
    # menu = build_menu_tree()
    if request.method == "GET":
        return render(request, 'add_service_line.html',locals())
    else:
        sl_name = request.POST.get('sl_name')
        obj = models.Service_Line.objects.create(service_line_name=sl_name)
        return redirect("/show_service_line")



def update_service_line(request):
    if request.method == "GET":
        sl_id = request.GET.get('id')
        sl_obj=models.Service_Line.objects.filter(id=sl_id).filter()[0]
        return render(request, 'update_service_line.html',locals())
    else:
        sl_id = request.POST.get('id')
        sl_name = request.POST.get('sl_name')
        print(sl_id,sl_name,request.POST)
        obj = models.Service_Line.objects.filter(id=sl_id).update(service_line_name=sl_name)
        return redirect("/show_service_line")



def del_service_line(request):
    sl_id = request.GET.get('id')
    sl_obj = models.Service_Line.objects.filter(id=sl_id).delete()
    return redirect("/show_service_line")









def add_host(request):
    menu = build_menu_tree()
    if request.method == "GET":
        host_form=HostForm()
        return render(request, 'add_host.html',locals())
    else:
        response = {'status': True, 'data': None, 'msg': None}
        host_form = HostForm(data=request.POST)
        if host_form.is_valid():
            host_form_data=host_form.cleaned_data
            host_ip = host_form_data["host_ip"]
            obj = models.host.objects
            if obj.filter(host_ip=host_ip):
                response['status'] = False
                response['msg'] ={'host_ip': ['ip不能重复']}
            else:
                obj=models.host.objects.create(**host_form.cleaned_data)
        else:
            response['status'] = False
            response['msg'] = host_form.errors
        return HttpResponse(json.dumps(response))


def del_host(request):
    host_id = request.GET.get('id')
    models.host.objects.filter(id=host_id).delete()
    return redirect("/index")




#def build_menu_tree(mn_list):



# def menu(request):
#     menu=build_menu_tree()
#     return  render(request,'menu.html',locals())
#
#
# def base(request):
#     menu=build_menu_tree()
#     return  render(request,'base.html',locals())




# def add_menu(request):
#     menu = build_menu_tree()
#     if request.method == "GET":
#         Menu_form = MenuForm()
#         return render(request, 'add_menu.html', locals())
#     else:
#         response = {'status': True, 'data': None, 'msg': None}
#         print(request.POST)
#         Menu_form = MenuForm(data=request.POST)
#         if Menu_form.is_valid():
#             obj = models.Menu.objects.create(**Menu_form.cleaned_data)
#                 # 数据库中添加一条数据
#                 # return redirect('/login.html') # ajax跳转，错错错
#         else:
#             response['status'] = False
#             response['msg'] = Menu_form.errors
#         return HttpResponse(json.dumps(response))


# def add_first_menu(request):
#     menu = build_menu_tree()
#     if request.method == "GET":
#         Menu_form = MenuForm()
#         return render(request, 'add_first_menu.html', locals())
#     else:
#         response = {'status': True, 'data': None, 'msg': None}
#         print(request.POST)
#         Menu_form = MenuForm(data=request.POST)
#         if Menu_form.is_valid():
#             obj = models.Menu.objects.create(**Menu_form.cleaned_data)
#                 # 数据库中添加一条数据
#                 # return redirect('/login.html') # ajax跳转，错错错
#         else:
#             response['status'] = False
#             response['msg'] = Menu_form.errors
#         return HttpResponse(json.dumps(response))






# def show_menu(request):
#     menu = build_menu_tree()
#     if request.method == "GET":
#         return render(request, 'show_menu.html', locals())


#
# @csrf_exempt
# def del_menu(request):
#         response = {'status': True, 'data': None, 'msg': None}
#         try:
#             id=request.POST.get("id")
#             obj = models.Menu.objects.filter(id=id).delete()
#         except Exception as e:
#             response['status'] = False
#             response['msg'] = e
#
#         return HttpResponse(json.dumps(response))




def add_app(request):
    menu = build_menu_tree()
    if request.method == "GET":
        app_form = appForm()
        return render(request, 'add_app.html', locals())
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