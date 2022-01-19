# Generated by Django 4.0.1 on 2022-01-13 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_exercise_category_exercise_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Chest', 'Chest'), ('Bicep', 'Bicep'), ('Tricep', 'Tricep'), ('Back', 'Back'), ('Legs', 'Legs'), ('Shoulders', 'Shoulders')], max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='category',
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscleGroup',
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscleGroup',
            field=models.ManyToManyField(null=True, to='api.MuscleGroup'),
        ),
    ]
