# Generated by Django 4.2.3 on 2023-07-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_alter_tour_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]