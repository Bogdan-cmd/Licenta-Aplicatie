# Generated by Django 3.1.7 on 2021-06-14 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20210614_2210'),
        ('posts', '0003_auto_20210614_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='groups.group', verbose_name='Grup'),
        ),
    ]
