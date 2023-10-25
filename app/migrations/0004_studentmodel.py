# Generated by Django 4.2.6 on 2023-10-25 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sessionyearmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('createat', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sessionid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='app.coursemodel')),
                ('sessionyear', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='app.sessionyearmodel')),
            ],
        ),
    ]
