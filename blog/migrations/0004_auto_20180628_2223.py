# Generated by Django 2.0.5 on 2018-06-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180628_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='relevance',
        ),
        migrations.RemoveField(
            model_name='input',
            name='status',
        ),
        migrations.AddField(
            model_name='input',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='input',
            name='waist',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='input',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
