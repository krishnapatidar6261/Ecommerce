# Generated by Django 4.2.3 on 2023-07-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0011_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
