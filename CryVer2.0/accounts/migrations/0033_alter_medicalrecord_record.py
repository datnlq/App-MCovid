# Generated by Django 3.2.8 on 2021-11-27 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_alter_medicalrecord_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='record',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='accounts.account'),
        ),
    ]
