# Generated by Django 4.1.7 on 2023-03-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0007_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]