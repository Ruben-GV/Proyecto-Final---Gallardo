# Generated by Django 4.1.7 on 2023-05-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_zapatilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abrigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=40)),
                ('talla', models.CharField(max_length=40)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('imagenAbrigo', models.ImageField(blank=True, null=True, upload_to='ropa')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
