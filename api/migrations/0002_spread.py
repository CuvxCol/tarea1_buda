# Generated by Django 4.1 on 2022-08-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spread',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('market_id', models.CharField(max_length=100)),
                ('spread', models.DecimalField(decimal_places=8, max_digits=20)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('lastChangeDate', models.DateTimeField(auto_now=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'spread',
                'managed': True,
            },
        ),
    ]
