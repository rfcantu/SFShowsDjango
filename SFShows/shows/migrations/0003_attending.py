# Generated by Django 3.2.2 on 2021-05-29 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20210514_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.CharField(max_length=30)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.show')),
            ],
        ),
    ]
