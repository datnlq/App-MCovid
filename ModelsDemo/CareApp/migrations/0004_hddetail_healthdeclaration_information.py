# Generated by Django 3.2.8 on 2021-10-26 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CareApp', '0003_sddetail_symptom_symptomdeclaration'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthDeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordID', models.CharField(blank=True, max_length=50, null=True)),
                ('DateModified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameInfo', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HDDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
                ('nameInfo', models.ManyToManyField(to='CareApp.Information')),
                ('recordID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CareApp.healthdeclaration')),
            ],
        ),
    ]
