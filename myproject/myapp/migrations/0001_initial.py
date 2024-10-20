# Generated by Django 5.1.2 on 2024-10-14 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HockeyClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('founded_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoachingStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('hockey_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaching_staff', to='myapp.hockeyclub')),
            ],
        ),
        migrations.AddField(
            model_name='hockeyclub',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.owner'),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('hockey_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='myapp.hockeyclub')),
            ],
        ),
    ]
