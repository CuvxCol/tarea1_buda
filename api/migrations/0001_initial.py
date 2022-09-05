# Generated by Django 4.1 on 2022-08-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spread',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('market_id', models.CharField(max_length=100)),
                ('spread', models.DecimalField(decimal_places=8, max_digits=20)),
                ('iso_code', models.CharField(max_length=5)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('lastChangeDate', models.DateTimeField(auto_now=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'spread',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('lastChangeDate', models.DateTimeField(auto_now=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'test',
                'managed': True,
            },
        ),
    ]