# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kernelciname', models.CharField(max_length=64)),
                ('lavaname', models.CharField(max_length=64)),
                ('arch', models.CharField(choices=[('arm', 'arm'), ('arm64', 'arm64'), ('x86', 'x86')], default='arm64', max_length=8)),
                ('deploytemplate', models.TextField(blank=True, null=True)),
                ('boottemplate', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KernelCIJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('branch', models.CharField(max_length=128)),
                ('squad_project_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TestTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('gitrepo', models.CharField(max_length=1024)),
                ('testname', models.CharField(max_length=1024)),
                ('parameters', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]