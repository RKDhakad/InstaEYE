# Generated by Django 4.0.5 on 2022-06-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackeddata',
            name='hacked_date',
            field=models.DateField(auto_now_add=True, verbose_name='Hacked Date'),
        ),
        migrations.AlterField(
            model_name='hackeddata',
            name='hacked_time',
            field=models.TimeField(auto_now_add=True, verbose_name='Hacked Time'),
        ),
    ]
