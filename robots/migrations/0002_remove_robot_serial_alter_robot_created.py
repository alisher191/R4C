# Generated by Django 4.2.5 on 2023-09-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='serial',
        ),
        migrations.AlterField(
            model_name='robot',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
