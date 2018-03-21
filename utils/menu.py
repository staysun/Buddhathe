#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "stay_sun"
from rbac import models




def build_menu_tree(request):
        response = {'status': True, 'data': None, 'msg': None}
        menu_tree_tpl=''
        parent_tpl='''<li class="treeview">
          <a href="#">
            <i class="fa fa-pie-chart"></i>
            <span> %s </span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>'''
        menu_tpl='''<li class="treeview">
                  <a href="#"><i class="fa fa-circle-o"></i> {{  second.caption }}
                    <span class="pull-right-container">
                      <i class="fa fa-angle-left pull-right"></i>
                    </span>
                  </a>
                  <ul class="treeview-menu">'''

        url_tpl='''<li><a href={{  second.url }}><i class="fa fa-circle-o"></i> {{  second.caption }}</a></li>'''


        email=request.session['email']
        user_obj =models.UserInfo.objects.filter(email=email).first()
        permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
                                              'permissions__menu_id').distinct()
        menu=[]
        for item in permission_item_list:
            menu_obj=models.Menu.objects.filter(id=item['permissions__menu_id'])
            parent=menu_obj.values('parent__caption','caption').first()
            parent.update(item)
            menu.append(parent)

        for line in menu:
            if line['parent__caption']:
                first_line=parent_tpl % (line['parent__caption'])
            else:
                first_line=parent_tpl % (line['caption'])
                url_line=url_tpl % (line['permissions__title'],line)




        print(menu)
        return response

        # def build_menu_data(li):
        #     dic = {}
        #     for item in li:
        #         item['children'] = []
        #         dic[item['id']] = item
        #
        #     result = []
        #     for item in li:
        #         pid = item['parent_id']
        #         if pid:
        #             dic[pid]['children'].append(item)
        #         else:
        #             result.append(item)
        #
        #     return result
        #
        # def build_menu_tree(mn_list):
        #     tpl1 = """
        #     <div class="item">
        #         <div class="title">{0}</div>
        #         <div class="body">{1}</div>
        #     </div>
        #     """
        #     tpl2 = "<a href={0}>{1}</a>"
        #
        #     html = ""
        #     for item in mn_list:
        #         if item['url']:
        #             html += tpl2.format(item['url'],item['caption'])
        #         else:
        #             if not item['children']:
        #                 html +=tpl1.format(item['caption'],"")
        #             else:
        #                 html +=tpl1.format(item['caption'],  build_menu_tree(item['children']))
        #     return html
        #
        # # def index(request):
        # #     from django.conf import settings
        # #     result = build_menu_data(settings.MENU_LIST)
        # #     html = build_menu_tree(result)
        # #     return render(request,'index.html',{'menu_html':html})


# def build_menu_tree():
#     mn_list=models.Menu.objects.all()
#     mn_dic={}
#     result = []
#     for item in mn_list:
#         item_message=item.__dict__
#         item_message['children'] = []
#         mn_dic[item_message['id']] = item_message
#
#         pid = item_message['parent_id']
#         if pid:
#             mn_dic[pid]['children'].append(item_message)
#         else:
#             result.append(item_message)
#     return result