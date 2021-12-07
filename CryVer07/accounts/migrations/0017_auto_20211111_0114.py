# Generated by Django 3.2.8 on 2021-11-10 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0016_auto_20211110_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acount',
            name='gender',
            field=models.CharField(choices=[('Nam', 'Nam'), ('Nu', 'Nữ')], default='Nữ', max_length=6),
        ),
        migrations.AlterField(
            model_name='acount',
            name='vaccination_status',
            field=models.CharField(choices=[('1', '1 mũi'), ('2', '2 mũi'), ('0', 'Chưa tiêm')], default='2 mũi', max_length=10),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChuyenKhoa', models.CharField(default='Chuyên khoa', max_length=50)),
                ('BenhVien', models.CharField(blank=True, default='Bệnh viện', max_length=50)),
                ('doctorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistantUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doctorUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
            ],
        ),
    ]
