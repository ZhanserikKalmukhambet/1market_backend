# Generated by Django 4.2 on 2023-04-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0, verbose_name='Rating')),
                ('address', models.CharField(max_length=255, verbose_name='Shop address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-rating', 'name'),
            },
        ),
    ]