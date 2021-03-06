# Generated by Django 3.0.3 on 2020-07-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_user_userpermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='权限名称')),
                ('url', models.CharField(max_length=255, verbose_name='URL名称')),
                ('per_method', models.SmallIntegerField(choices=[(1, 'GET'), (2, 'POST')], default=1, verbose_name='请求方法')),
                ('argument_list', models.CharField(blank=True, help_text='多个参数之间用英文半角逗号隔开', max_length=255, null=True, verbose_name='参数列表')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
            ],
            options={
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
                'permissions': (('views_search_cities', '查看学员详细信息'),),
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.CharField(max_length=8, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userPassword',
            field=models.CharField(max_length=20, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userPermission',
            field=models.BooleanField(default=False, verbose_name='用户权限'),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('Permissions', models.ManyToManyField(to='weather.Permission')),
            ],
        ),
    ]
