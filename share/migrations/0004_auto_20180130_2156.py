# Generated by Django 2.0.1 on 2018-01-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20180130_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=300),
        ),
    ]
