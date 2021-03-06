# Generated by Django 2.2.1 on 2019-05-17 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name="author's first name")),
                ('last_name', models.CharField(max_length=50, verbose_name="author's last name")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name="book's title")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Author')),
            ],
        ),
    ]
