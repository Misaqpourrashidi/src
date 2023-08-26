# Generated by Django 3.2 on 2023-05-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('product_title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=350, unique=True)),
                ('check', models.BooleanField(blank=True, default=False)),
                ('number_product', models.FloatField()),
            ],
        ),
    ]