# Generated by Django 3.1.7 on 2021-04-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_auto_20210404_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='student_academicLevel',
            new_name='academicLevel',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_contactno',
            new_name='contactno',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_last_name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]