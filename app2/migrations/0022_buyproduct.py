# Generated by Django 4.1.7 on 2023-04-08 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0021_addtrasctions_alter_client_client_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('supplyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.suplyer')),
            ],
        ),
    ]