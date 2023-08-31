# Generated by Django 4.2.3 on 2023-08-30 17:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_yazar_start_date_alter_yazar_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazar',
            name='category',
            field=models.CharField(choices=[('ekonomi', 'ekonomi'), ('mutfak', 'mutfak'), ('teknoloji', 'teknoloji'), ('hikaye', 'hikaye')], default='teknoloji', max_length=100),
        ),
        migrations.AlterField(
            model_name='yazar',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 30, 17, 19, 6, 218160, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Yazi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(default='', max_length=100)),
                ('icerik', models.TextField(default='', max_length=2000)),
                ('image', models.ImageField(upload_to='yazilar/')),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]