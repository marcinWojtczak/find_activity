# Generated by Django 4.0.5 on 2022-07-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='activity',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
