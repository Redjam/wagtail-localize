# Generated by Django 3.0.6 on 2020-07-08 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_test', '0010_auto_20200708_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testchildobject',
            name='is_source_translation',
        ),
        migrations.RemoveField(
            model_name='testhomepage',
            name='is_source_translation',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='is_source_translation',
        ),
        migrations.RemoveField(
            model_name='testnonparentalchildobject',
            name='is_source_translation',
        ),
        migrations.RemoveField(
            model_name='testpage',
            name='is_source_translation',
        ),
        migrations.RemoveField(
            model_name='testsnippet',
            name='is_source_translation',
        ),
    ]
