# Generated by Django 5.1.1 on 2024-11-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('street_number', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('apartment_number', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
                ('party_affiliation', models.CharField(max_length=30)),
                ('precinct_number', models.CharField(max_length=30)),
                ('v20state', models.BooleanField()),
                ('v21town', models.BooleanField()),
                ('v21primary', models.BooleanField()),
                ('v22general', models.BooleanField()),
                ('v23town', models.BooleanField()),
                ('voter_score', models.IntegerField()),
            ],
        ),
    ]