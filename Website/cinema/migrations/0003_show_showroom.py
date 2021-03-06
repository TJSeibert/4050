# Generated by Django 2.2.7 on 2019-11-20 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_auto_20191118_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('showroom_id', models.IntegerField(primary_key=True, serialize=False)),
                ('numSeats', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('show_id', models.IntegerField(primary_key=True, serialize=False)),
                ('scheduledTime', models.TimeField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Movie')),
                ('showroom_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.Showroom')),
            ],
        ),
    ]
