# Generated by Django 3.1.2 on 2021-02-19 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upimagesu',
            options={'ordering': ('-title',)},
        ),
        migrations.RemoveField(
            model_name='upimagesu',
            name='create',
        ),
        migrations.RemoveField(
            model_name='upimagesu',
            name='visit',
        ),
    ]