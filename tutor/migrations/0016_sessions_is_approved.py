# Generated by Django 3.1.7 on 2021-04-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0015_auto_20210412_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]