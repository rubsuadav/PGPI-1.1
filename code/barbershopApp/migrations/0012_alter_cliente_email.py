# Generated by Django 4.1.3 on 2022-11-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopApp', '0011_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
