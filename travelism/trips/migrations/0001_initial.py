# Generated by Django 3.0.1 on 2020-02-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('price', models.FloatField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('requirements', models.TextField()),
                ('payment_methods', models.TextField()),
            ],
        ),
    ]