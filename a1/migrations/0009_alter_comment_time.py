# Generated by Django 4.2.3 on 2023-07-30 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0008_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
