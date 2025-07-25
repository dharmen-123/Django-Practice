# Generated by Django 5.2.3 on 2025-06-26 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app9th', '0003_alter_client_table_alter_employee_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('basedata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app9th.basedata')),
                ('empid', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
            bases=('app9th.basedata',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('basedata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app9th.basedata')),
                ('Branch', models.CharField()),
                ('fees', models.IntegerField()),
            ],
            bases=('app9th.basedata',),
        ),
    ]
