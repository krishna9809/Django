# Generated by Django 5.0.7 on 2024-07-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_alter_teacher_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
