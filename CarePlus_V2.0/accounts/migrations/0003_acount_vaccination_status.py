# Generated by Django 3.2.8 on 2021-11-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211110_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='acount',
            name='vaccination_status',
            field=models.CharField(default=[('1', '1 mũi'), ('2', '2 mũi'), ('0', 'Chưa tiêm')], max_length=2),
        ),
    ]
