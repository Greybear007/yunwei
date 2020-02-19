from django.db import models
# Create your models here.


class Env():
    REAL = 1
    DEMO = 2
    TEST = 3 
    ENV = (
        (REAL, '实盘'),
        (DEMO, '模拟盘'),
        (TEST, '测试盘'),
    )


class Exchange(models.Model):

    class Meta:
        verbose_name = "交易所"
        verbose_name_plural = "交易所"

    short_name = models.CharField(max_length=128, verbose_name='简称')
    full_name = models.CharField(max_length=256, verbose_name='全称')
    english_name = models.CharField(max_length=512, verbose_name='英文名称')
    comment = models.TextField(verbose_name='简介', help_text='正文必须是markdown格式')
    project_manager = models.CharField(max_length=1024, verbose_name='项目经理')
    client = models.CharField(max_length=1024, verbose_name='对接客户',)
    operator = models.CharField(max_length=1024, verbose_name='运维人员' )
    bussiness_mode = models.CharField(max_length=1024, verbose_name='业务模式')

    def __str__(self):
        return self.short_name
    

class Bookkeeping(models.Model):

    class Meta:
        verbose_name = "台账"
        verbose_name_plural = "台账"

    def __str__(self):
        pass

    hostname = models.CharField(max_length=64, verbose_name='主机名')
    private_ip = models.CharField(max_length=64, verbose_name='内网ip')
    internet_ip = models.CharField(max_length=64, verbose_name='外网ip')
    usage = models.CharField(max_length=128, verbose_name='用途')
    operating_system = models.CharField(max_length=32, verbose_name='操作系统')
    net_port = models.CharField(max_length=64, verbose_name='防火墙端口')
    cpu = models.CharField(max_length=64, verbose_name='处理器')
    memory = models.CharField(max_length=64, verbose_name='内存')
    username = models.CharField(max_length=64, verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')
    exchange = models.ForeignKey(Exchange, verbose_name='交易所', on_delete=models.CASCADE)
    environment = models.PositiveIntegerField(choices=Env.ENV, verbose_name='环境')
    remarks = models.TextField(verbose_name='备注', help_text='正文必须是markdown格式')

  
class Stuff(models.Model):

    class Meta:
        verbose_name = "备注"
        verbose_name_plural = "备注"

    def __str__(self):
        pass

    item = models.CharField(max_length=64, verbose_name='项目')
    usage = models.CharField(max_length=64, verbose_name='用途')
    url = models.CharField(max_length=64, verbose_name='链接')
    username = models.CharField(max_length=64, verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')
    exchange = models.ForeignKey(Exchange, verbose_name='交易所', on_delete=models.CASCADE)
    environment = models.PositiveIntegerField(choices=Env.ENV, verbose_name='环境')
    remarks = models.TextField(verbose_name='备注', help_text='正文必须是markdown格式')


class Net_transfer(models.Model):

    class Meta:
        verbose_name = "网络转发"
        verbose_name_plural = "网络转发"

    def __str__(self):
        pass

    private_ip = models.CharField(max_length=64, verbose_name='内网ip')
    private_port = models.CharField(max_length=64, verbose_name='内网端口')
    internet_ip = models.CharField(max_length=64, verbose_name='外网ip') 
    internet_port = models.CharField(max_length=64, verbose_name='外网端口')
    internet_url = models.URLField(verbose_name='外网域名')
    transfer_id = models.CharField(max_length=64, verbose_name='转发ip') 
    transfer_port = models.CharField(max_length=64, verbose_name='转发端口')
    transfer_url = models.URLField(verbose_name='转发域名')
    exchange = models.ForeignKey(Exchange, verbose_name='交易所', on_delete=models.CASCADE)
    environment = models.PositiveIntegerField(choices=Env.ENV, verbose_name='环境')
    remarks = models.TextField(verbose_name='备注', help_text='正文必须是markdown格式')


