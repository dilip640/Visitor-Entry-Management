# Generated by Django 2.2.7 on 2019-12-01 14:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('entryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Host Name'),
        ),
        migrations.AlterField(
            model_name='host',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN', verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='pastvisitor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN', verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN', unique=True, verbose_name='Phone'),
        ),
    ]
