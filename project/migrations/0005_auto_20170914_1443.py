# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20170914_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='need_skills',
            field=models.ManyToManyField(blank=True, to='project.Skill', verbose_name='\u0422\u0440\u0435\u0431\u0443\u0435\u043c\u044b\u0435 \u043d\u0430\u0432\u044b\u043a\u0438'),
        ),
    ]