# Generated by Django 4.1.7 on 2023-04-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0015_checkout_possale'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddExpenseMony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Money', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
