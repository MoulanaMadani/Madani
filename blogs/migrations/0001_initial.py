# Generated by Django 2.2 on 2020-04-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Date', models.DateField()),
                ('Body', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]