# Generated by Django 4.1.7 on 2023-04-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0022_buyproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]