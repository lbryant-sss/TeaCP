# Generated by Django 3.2.13 on 2022-05-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20220502_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='intro',
            field=models.TextField(max_length=2555, null=True),
        ),
    ]