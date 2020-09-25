# Generated by Django 3.1.1 on 2020-09-25 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_description', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('expires_on', models.DateField()),
                ('is_Expired', models.BooleanField(default=False)),
                ('goal_amount', models.IntegerField()),
                ('received_amount', models.IntegerField(default=0)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]