# Generated by Django 2.0.5 on 2018-06-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180629_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extraversion', models.CharField(choices=[('1', 'Reservado'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Carismático')], default='1', max_length=1)),
                ('neuroticism', models.CharField(choices=[('1', 'Nervoso'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Confiante')], default='1', max_length=1)),
                ('agreeableness', models.CharField(choices=[('1', 'Não-amigável'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Amigável')], default='1', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Input',
        ),
    ]
