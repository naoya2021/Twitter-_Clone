# Generated by Django 2.2.27 on 2022-03-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.NewTweet')),
            ],
        ),
    ]
