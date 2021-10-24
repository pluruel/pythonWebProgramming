# Generated by Django 3.2.8 on 2021-10-23 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='NAME')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='On Line Description')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['title'], 'verbose_name': 'my faveorite Name', 'verbose_name_plural': 'my faveorite Names'},
        ),
        migrations.AlterModelManagers(
            name='bookmark',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelTable(
            name='bookmark',
            table='bookmark',
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('albums', models.ManyToManyField(to='bookmark.Album')),
            ],
        ),
    ]
