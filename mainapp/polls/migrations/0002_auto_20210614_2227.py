# Generated by Django 3.1.7 on 2021-06-14 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_four',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_three',
            field=models.CharField(max_length=50),
        ),
    ]
