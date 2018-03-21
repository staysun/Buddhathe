#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "stay_sun"



from pyzabbix import ZabbixAPI



def login():
    zapi = ZabbixAPI("http://dbmonitor.ky.com/zabbix/")    #server是指zabbixweb界面的url，比如http://192.168.1.101/zabbix
    zapi.login("sun","123456")    #指的是zabbix系统里的用户名和密码，不是服务器本身的用户名和密码
    return zapi

def get_hostgroups(group_name):
    return zapi.hostgroup.get(search={"name": group_name}, output="extend")  # 搜索输入的组别，提取组id


def get_hosts(groupid):
    groupids = [groupid]
    return zapi.host.get(groupids=groupids, output="extend")  # 返回该组id 下的所有host 信息


def get_drules():
    return zapi.drule.get(output="extend")


def get_templates_by_names(template_names):
    return zapi.template.get(filter={"host": template_names})


def create_group(group_name):  # 创建组
    if not zapi.hostgroup.exists(name=group_name):
        zapi.hostgroup.create(name=group_name)


def create_host(group_name, host_name, ip):  # 创建主机并附加指定模板
    groups = get_hostgroups(group_name)
    host_name = host_name.lower()
    ip_tail = ip.split(".")[-1]
    domain = "server-" + ip_tail + ".0." + host_name + ".ustack.in"
    for hostgroup in groups:
        groupid = hostgroup['groupid']
        ip_tail = ip.split(".")[-1]
        role = None
        for ru in rule:
            range = rule[ru]['range']
            if "-" in range:
                head = range.split("-")[0]
                tail = range.split("-")[1]
                if int(ip_tail) <= int(tail) and int(ip_tail) >= int(head):
                    role = ru
            else:
                if ip_tail == range:
                    role = ru
        template_names = rule[role]['templates']
        template_ids = get_templates_by_names(template_names)
        print(domain, ip, groupid, template_ids)
        zapi.host.create(host=domain, interfaces=[{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": '10050'
        }], groups=[{"groupid": groupid}], templates=template_ids)
        print("Add Successfull!!!!!")
        # logging.info("%s,%s,%s,%s Add Successfull!!!!!"%(domain,ip,groupid,template_ids))



if __name__ == "__main__":
    zapi = login()
    zapi.
    host_groups=get_hostgroups('T2-PROD-Zabbix1')
    hosts=get_hosts('T2-PROD-Zabbix1')
    print(host_groups,hosts)
    # host = get_hosts(host_groups[0]['groupid'])
    # # print(host,host_groups[0]['groupid'])
    # # zapi.item.create(host='')
    # zapi.item.create(host='prod-zabbix01_server', interfaces=[{
    #     "name": 'dfb-mysql-01-22',
    #     "type": 1,
    #     "key": 'Health.NetService[11.0.3.111,10050]',
    #     "hostid": "30074",
    #     "delay": 30
    # }], groups=[{"groupid": host_groups[0]['groupid']}], templates='Template_Zabbix-T1')
    # print("Add Successfull!!!!!")
