# Generated by Django 3.1.6 on 2021-04-02 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_name', models.CharField(max_length=100)),
                ('tournament_type', models.BooleanField()),
                ('tournament_class', models.CharField(max_length=100)),
                ('tournament_total_team', models.CharField(blank=True, max_length=100)),
                ('tournament_template', models.CharField(blank=True, max_length=100)),
                ('tournament_detials', models.CharField(blank=True, max_length=100)),
                ('lat', models.IntegerField(blank=True, max_length=200)),
                ('lon', models.IntegerField(blank=True, max_length=200)),
                ('start_date', models.DateField(blank=True, max_length=200)),
                ('end_date', models.DateField(blank=True, max_length=200)),
            ],
        ),
    ]