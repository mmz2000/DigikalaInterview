# Generated by Django 4.1.1 on 2022-09-23 09:48

import datetime
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
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Name')),
                ('rss_url', models.URLField(verbose_name='RSS URL')),
                ('max_saved_items', models.IntegerField(verbose_name='Max Saved Items')),
                ('refresh_rate', models.DurationField(choices=[(datetime.timedelta(seconds=3600), '1 hour'), (datetime.timedelta(seconds=7200), '2 hours'), (datetime.timedelta(seconds=21600), '6 hours'), (datetime.timedelta(seconds=43200), '12 hours'), (datetime.timedelta(days=1), '1 day')], default=datetime.timedelta(seconds=3600), verbose_name='Refresh Rate')),
                ('favorited_by', models.ManyToManyField(related_query_name='favorite_feeds', to=settings.AUTH_USER_MODEL, verbose_name='Favorited By')),
            ],
            options={
                'verbose_name': 'Feed',
                'verbose_name_plural': 'Feeds',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('url', models.URLField(verbose_name='URL')),
                ('published_at', models.DateTimeField(verbose_name='Published At')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.feed', verbose_name='Feed')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]