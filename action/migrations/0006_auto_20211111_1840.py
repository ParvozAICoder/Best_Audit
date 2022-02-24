# Generated by Django 3.2.9 on 2021-11-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0005_body_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='body',
        ),
        migrations.AddField(
            model_name='rate',
            name='first',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='second',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='third',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='prize',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Body',
        ),
    ]