from django.conf import settings
from .. import models
import json
# 保存用户权限的Session Key
SESSION_PERMISSION_URL_KEY = "afikjmdlalemnasldkfaeasfd"

SESSION_PERMISSION_MENU_URL_KEY = "sdfasd3234xdfsdf23sdfsdf"
ALL_MENU_KEY = "k1"
PERMISSION_URL_KEY = "k2"



def init_permission(request, user_obj):
    """
    初始化用户权限
    :param request:获取session  使用
    :param user_obj:用户对象
    :return:
    """
    permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
                                                 'permissions__menu_id').distinct()
    # print(permission_item_list)

    # 保存当前用户有权访问的URL
    permission_url_list = []

    # 保存当前用户有权访问的URL且需要在菜单上显示
    permission_menu_list = []

    for item in permission_item_list:
        permission_url_list.append(item['permissions__url'])
        if item['permissions__menu_id']:
            temp = {'title': item['permissions__title'], 'url': item['permissions__url'],
                    'menu_id': item['permissions__menu_id']}
            permission_menu_list.append(temp)

    # 所有菜单
    menu_list = list(models.Menu.objects.values('id','caption', 'parent_id'))

    # print(menu_list)
    # print(permission_item_list)
    request.session[settings.SESSION_PERMISSION_URL_KEY] = permission_url_list

    request.session[settings.SESSION_PERMISSION_MENU_URL_KEY] = {
        settings.PERMISSION_URL_KEY: permission_menu_list,
        settings.ALL_MENU_KEY: menu_list,
    }

    #
    #
    # result = []
    # mn_dic = {}
    # for item in menu_list:
    #     if item['id'] ==
    #     item['children'] = []
    #     mn_dic[item['id']] = item
    #     pid = item['parent_id']
    #     if pid:
    #          mn_dic[pid]['children'].append(item)
    #     else:
    #          result.append(item)
    # print(mn_dic)
    # print(result)
    # import json
    # json.dumps(result)
    # return result

# def init_permission_bak(request, user_obj):
#     """
#     初始化用户权限
#     :param request:获取session  使用
#     :param user_obj:用户对象
#     :return:
#     """
#     permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
#                                                  'permissions__menu_id').distinct()
#
#     # 保存当前用户有权访问的URL
#     permission_url_list = []
#
#     # 保存当前用户有权访问的URL且需要在菜单上显示
#     permission_menu_list = []
#
#     for item in permission_item_list:
#         permission_url_list.append(item['permissions__url'])
#         if item['permissions__menu_id']:
#             temp = {'title': item['permissions__title'], 'url': item['permissions__url'],
#                     'menu_id': item['permissions__menu_id']}
#             permission_menu_list.append(temp)
#
#     # 所有菜单
#     menu_list = list(models.Menu.objects.values('caption', 'parent_id'))
#
#     request.session[settings.SESSION_PERMISSION_URL_KEY] = permission_url_list
#
#     request.session[settings.SESSION_PERMISSION_MENU_URL_KEY] = {
#         settings.PERMISSION_URL_KEY: permission_menu_list,
#         settings.ALL_MENU_KEY: menu_list,
#     }



def build_menu_tree(request):
    '''一级菜单 不设置权限  只是展示
        二级菜单可以设置权限
        三级菜单 直接只有功能  也就是权限
    '''
    email=request.session['email']
    user_obj =models.UserInfo.objects.filter(email=email).first()
    permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
                                          'permissions__menu_id').distinct()
    ##
    menu_dic=[]
    for item in permission_item_list:
        menu_obj=models.Menu.objects.filter(id=item['permissions__menu_id'])
        parent=menu_obj.values('parent__caption','caption').first()
        parent.update(item)
        menu_dic.append(parent)
    return json.dumps(menu_dic)

