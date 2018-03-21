from django.db import models

# Create your models here.




class app(models.Model):
    app_name=models.CharField(max_length=64)
    remark=models.CharField(max_length=128,null=True)#备注



class hardware(models.Model):
    motor_room=models.CharField(max_length=64)#机房地址
    motor_room_num = models.CharField(max_length=64)#机房名称
    Cabinet=models.CharField(max_length=64)#机柜
    sn_no=models.CharField(max_length=64)#sn号
    remark = models.CharField(max_length=128, null=True)#备注



class host(models.Model):
    hostname=models.CharField(max_length=64,null=True)
    host_ip=models.CharField(max_length=20,unique=True)
    ssh_port=models.CharField(max_length=4,default="22")
    cpu=models.IntegerField(null=True)
    mem=models.DecimalField(max_digits=8, decimal_places=2)#总位数 8位  可以有俩位小数
    OS_version=models.CharField(max_length=20,unique=True)#操作系统版本
    is_vm=models.BooleanField() #判断是否为 vm  真或者假
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    app=models.ManyToManyField(app)#应用信息
    hardware=models.ManyToManyField(hardware) #硬件信息
#    disk = models.CharField(max_length=64,null=True) 需要处理相关信息




class Service_Line(models.Model):
    service_line_name = models.CharField(max_length=50)


# class User(models.Model):
#     username=models.CharField(max_length=32)
#     password=models.CharField(max_length=64)
#     email=models.EmailField()
#     phone=models.CharField(max_length=11,null=True)
#     sl=models.ManyToManyField(Service_Line)




# class  Menu(models.Model):
#     caption = models.CharField(max_length=32)
#     #is_menu = models.BooleanField(default=False)
#     url = models.CharField(max_length=128, null=True, blank=True,default=0)
#     parent = models.ForeignKey('Menu', related_name='pid', null=True, blank=True)


