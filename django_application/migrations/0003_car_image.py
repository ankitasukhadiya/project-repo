# Generated by Django 4.1.1 on 2022-09-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_application', '0002_buycar_commission_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
