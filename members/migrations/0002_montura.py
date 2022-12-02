# Generated by Django 4.1.3 on 2022-12-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Montura',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('velocidad', models.IntegerField(default=20)),
                ('aventurero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='members.aventurero')),
            ],
        ),
    ]
