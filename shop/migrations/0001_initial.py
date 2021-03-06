# Generated by Django 3.0.2 on 2020-02-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
