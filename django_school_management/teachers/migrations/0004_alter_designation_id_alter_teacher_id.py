# Generated by Django 4.2.3 on 2023-07-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teacher_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]