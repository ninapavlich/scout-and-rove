# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='test',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='set',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testsetting',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='testsetting',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='testsetting',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='testsetting',
            name='test',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TestResult',
        ),
        migrations.DeleteModel(
            name='TestSetting',
        ),
    ]
