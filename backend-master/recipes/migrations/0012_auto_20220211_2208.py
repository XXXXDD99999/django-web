# Generated by Django 3.2.11 on 2022-02-11 22:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20220211_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='nutrient',
        ),
        migrations.AddField(
            model_name='nutrient',
            name='recipe',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
            preserve_default=False,
        ),
    ]