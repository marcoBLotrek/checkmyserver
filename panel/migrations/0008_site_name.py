# Generated by Django 2.1.3 on 2018-11-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_auto_20181122_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(default=models.CharField(max_length=200), max_length=200),
        ),
    ]
