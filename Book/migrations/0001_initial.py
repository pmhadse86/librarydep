# Generated by Django 3.2.5 on 2021-08-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('is_published', models.BooleanField(default=False)),
                ('published_date', models.DateField(null=True)),
                ('is_deleted', models.CharField(default='N', max_length=1)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
