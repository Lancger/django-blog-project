# Generated by Django 3.1.1 on 2020-09-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_blogcomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='object_pk',
            field=models.IntegerField(verbose_name='object ID'),
        ),
    ]
