# Generated by Django 5.0.3 on 2024-03-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('active', 'Активний'), ('finished', 'Фінішед'), ('cancelled', 'Скасований')], default='active', max_length=20),
        ),
    ]
