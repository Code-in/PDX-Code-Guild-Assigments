# Generated by Django 3.1.5 on 2021-03-05 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210304_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(default='Medium', on_delete=django.db.models.deletion.CASCADE, to='todo.priority'),
        ),
    ]
