# Generated by Django 3.1 on 2020-09-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
    ]
