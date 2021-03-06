# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-02 07:21
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, help_text='\u7528\u6237\u540d', max_length=20, null=True, unique=True)),
                ('cellphone', models.CharField(blank=True, help_text='\u624b\u673a\u53f7\u7801', max_length=20, null=True)),
                ('sex', models.SmallIntegerField(choices=[(0, b'\xe4\xbf\x9d\xe5\xaf\x86'), (1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')], default=0, help_text='\u6027\u522b')),
                ('signature', models.CharField(blank=True, help_text='\u7b7e\u540d', max_length=30, null=True)),
                ('authority', models.SmallIntegerField(choices=[(0, b'\xe6\x99\xae\xe9\x80\x9a\xe7\x94\xa8\xe6\x88\xb7'), (1, b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98'), (2, b'\xe8\xb6\x85\xe7\xba\xa7\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')], default=0, help_text='\u6743\u9650')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('name', models.CharField(blank=True, help_text='\u57ce\u5e02\u540d', max_length=20, null=True)),
                ('create_user', models.ForeignKey(blank=True, help_text='\u521b\u5efa\u4eba', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_city_create_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('name', models.CharField(blank=True, help_text='\u7701\u540d', max_length=20, null=True)),
                ('create_user', models.ForeignKey(blank=True, help_text='\u521b\u5efa\u4eba', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_province_create_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Province',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('schoolname', models.CharField(blank=True, help_text='\u5b66\u6821\u540d\u79f0', max_length=20, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.City')),
                ('create_user', models.ForeignKey(blank=True, help_text='\u521b\u5efa\u4eba', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_school_create_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Province'),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.School'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
