# Generated by Django 4.1.7 on 2023-03-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_client_alter_productinput_price_possale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='possale',
            name='client_name',
        ),
    ]
