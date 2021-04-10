# Generated by Django 3.1.7 on 2021-04-10 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletjournal', '0005_auto_20210409_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Today',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletjournal.key')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletjournal.name')),
            ],
        ),
    ]