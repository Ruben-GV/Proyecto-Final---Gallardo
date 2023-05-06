# Generated by Django 4.1.7 on 2023-05-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_pantalon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=40)),
                ('talla', models.CharField(max_length=40)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('imagenZapato', models.ImageField(blank=True, null=True, upload_to='ropa')),
            ],
        ),
    ]