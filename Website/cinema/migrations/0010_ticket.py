# Generated by Django 2.2.7 on 2019-12-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0009_auto_20191120_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketID', models.IntegerField(primary_key=True, serialize=False)),
                ('ageType', models.CharField(choices=[('Child', 'Child'), ('Adult', 'Adult'), ('Senior', 'Senior')], max_length=100)),
            ],
        ),
    ]