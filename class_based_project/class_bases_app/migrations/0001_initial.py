# Generated by Django 5.0.3 on 2024-03-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('lname', models.CharField(max_length=45)),
                ('sal', models.FloatField()),
            ],
        ),
    ]