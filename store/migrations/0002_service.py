# Generated by Django 4.1.1 on 2022-10-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('petrols', models.ManyToManyField(related_name='services', to='store.petrolstore', verbose_name='АЗС')),
            ],
            options={
                'verbose_name': 'Дополнительные услуги',
                'verbose_name_plural': 'Список дополнительных услуг',
            },
        ),
    ]
