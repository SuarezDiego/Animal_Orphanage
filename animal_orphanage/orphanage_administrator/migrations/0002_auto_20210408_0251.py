# Generated by Django 3.1.7 on 2021-04-08 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage_administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='date_adoption',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_found',
            field=models.DateField(),
        ),
    ]
