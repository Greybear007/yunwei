# Generated by Django 3.0.3 on 2020-02-19 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=128, verbose_name='简称')),
                ('full_name', models.CharField(max_length=256, verbose_name='全称')),
                ('english_name', models.CharField(max_length=512, verbose_name='英文名称')),
                ('comment', models.TextField(help_text='正文必须是markdown格式', verbose_name='简介')),
                ('project_manager', models.CharField(max_length=1024, verbose_name='项目经理')),
                ('client', models.CharField(max_length=1024, verbose_name='对接客户')),
                ('operator', models.CharField(max_length=1024, verbose_name='运维人员')),
                ('bussiness_mode', models.CharField(max_length=1024, verbose_name='业务模式')),
            ],
            options={
                'verbose_name': '交易所',
                'verbose_name_plural': '交易所',
            },
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64, verbose_name='项目')),
                ('usage', models.CharField(max_length=64, verbose_name='用途')),
                ('url', models.CharField(max_length=64, verbose_name='链接')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('environment', models.PositiveIntegerField(choices=[(1, '实盘'), (2, '模拟盘'), (3, '测试盘')], verbose_name='环境')),
                ('remarks', models.TextField(help_text='正文必须是markdown格式', verbose_name='备注')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Exchange', verbose_name='交易所')),
            ],
            options={
                'verbose_name': '备注',
                'verbose_name_plural': '备注',
            },
        ),
        migrations.CreateModel(
            name='Net_transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_ip', models.CharField(max_length=64, verbose_name='内网ip')),
                ('private_port', models.CharField(max_length=64, verbose_name='内网端口')),
                ('internet_ip', models.CharField(max_length=64, verbose_name='外网ip')),
                ('internet_port', models.CharField(max_length=64, verbose_name='外网端口')),
                ('internet_url', models.URLField(verbose_name='外网域名')),
                ('transfer_id', models.CharField(max_length=64, verbose_name='转发ip')),
                ('transfer_port', models.CharField(max_length=64, verbose_name='转发端口')),
                ('transfer_url', models.URLField(verbose_name='转发域名')),
                ('environment', models.PositiveIntegerField(choices=[(1, '实盘'), (2, '模拟盘'), (3, '测试盘')], verbose_name='环境')),
                ('remarks', models.TextField(help_text='正文必须是markdown格式', verbose_name='备注')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Exchange', verbose_name='交易所')),
            ],
            options={
                'verbose_name': '网络转发',
                'verbose_name_plural': '网络转发',
            },
        ),
        migrations.CreateModel(
            name='Bookkeeping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, verbose_name='主机名')),
                ('private_ip', models.CharField(max_length=64, verbose_name='内网ip')),
                ('internet_ip', models.CharField(max_length=64, verbose_name='外网ip')),
                ('usage', models.CharField(max_length=128, verbose_name='用途')),
                ('operating_system', models.CharField(max_length=32, verbose_name='操作系统')),
                ('net_port', models.CharField(max_length=64, verbose_name='防火墙端口')),
                ('cpu', models.CharField(max_length=64, verbose_name='处理器')),
                ('memory', models.CharField(max_length=64, verbose_name='内存')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('environment', models.PositiveIntegerField(choices=[(1, '实盘'), (2, '模拟盘'), (3, '测试盘')], verbose_name='环境')),
                ('remarks', models.TextField(help_text='正文必须是markdown格式', verbose_name='备注')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Exchange', verbose_name='交易所')),
            ],
            options={
                'verbose_name': '台账',
                'verbose_name_plural': '台账',
            },
        ),
    ]
