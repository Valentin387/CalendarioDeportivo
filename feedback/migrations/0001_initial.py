# Generated by Django 4.1.3 on 2022-11-24 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(max_length=10)),
                ('Sport', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Star_H', models.FloatField()),
                ('Star_R', models.FloatField()),
                ('Star_T', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Match_field', to='feedback.event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Match_field', to='feedback.profile')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Event_creator', to='feedback.profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='Field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Match_field', to='feedback.field'),
        ),
    ]
