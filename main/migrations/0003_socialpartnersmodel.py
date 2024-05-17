# Generated by Django 5.0.6 on 2024-05-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_graduateinfomodel_pril_kaz_graduateinfomodel_pril_ru'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPartnersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(upload_to='uploads/graduate/social_partners', verbose_name='Логотип партнера')),
            ],
            options={
                'verbose_name': 'Логотип',
                'verbose_name_plural': 'Логотипы',
            },
        ),
    ]
