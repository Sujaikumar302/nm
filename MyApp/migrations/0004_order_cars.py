# Generated by Django 4.0.4 on 2022-07-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cars',
            field=models.CharField(default='', max_length=50),
        ),
    ]