# Generated by Django 5.0.6 on 2024-05-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_socialpartnersmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='specmodel',
            name='sokr_spec_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Сокращенно'),
        ),
        migrations.AlterField(
            model_name='specmodel',
            name='spec_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Специальность'),
        ),
    ]