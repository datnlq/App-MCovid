# Generated by Django 3.2.8 on 2021-12-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20211130_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(default='card.svg', upload_to='', verbose_name='Ảnh đại diện'),
        ),
    ]
