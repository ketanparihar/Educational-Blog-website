# Generated by Django 3.1.5 on 2021-04-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210410_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]