# Generated by Django 2.1.4 on 2018-12-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181216_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_order',
            name='user',
            field=models.CharField(max_length=64),
        ),
    ]