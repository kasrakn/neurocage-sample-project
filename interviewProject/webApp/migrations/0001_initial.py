# Generated by Django 4.2.1 on 2023-05-20 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('health_status', models.IntegerField(null=True)),
                ('is_successful', models.BooleanField()),
                ('cage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_data_rows', to='webApp.cage')),
            ],
        ),
    ]