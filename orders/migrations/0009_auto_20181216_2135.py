# Generated by Django 2.1.4 on 2018-12-16 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_user_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order2',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User_order'),
        ),
    ]
