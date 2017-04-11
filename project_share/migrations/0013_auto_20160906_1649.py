# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_share', '0012_auto_20160901_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='when_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='when_modified',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='application_type',
            field=models.CharField(choices=[(b'CSNAP', b'cSnap'), (b'BLOCK', b'Blockly/Scratch')], max_length=5),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username'),
        ),
    ]
