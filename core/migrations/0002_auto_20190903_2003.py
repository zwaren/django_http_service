# Generated by Django 2.1.7 on 2019-09-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='house',
            field=models.IntegerField(),
        ),
    ]