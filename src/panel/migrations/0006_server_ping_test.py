# Generated by Django 2.1.3 on 2018-11-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_auto_20181116_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='ping_test',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]
