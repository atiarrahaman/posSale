# Generated by Django 4.1.7 on 2023-03-04 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinput',
            name='item_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productInputs', to='app2.product'),
        ),
        migrations.AlterField(
            model_name='productinput',
            name='sypplyer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppylers', to='app2.suplyer'),
        ),
        migrations.CreateModel(
            name='ProductInputCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.productinput')),
            ],
        ),
    ]
