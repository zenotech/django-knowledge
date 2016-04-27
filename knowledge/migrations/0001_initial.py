# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('alert', models.BooleanField(default=True, help_text='Check this if you want to be alerted when a new response is added.', verbose_name='Alert')),
                ('name', models.CharField(help_text='Enter your first and last name.', max_length=64, null=True, verbose_name='Name', blank=True)),
                ('email', models.EmailField(help_text='Enter a valid email address.', max_length=254, null=True, verbose_name='Email', blank=True)),
                ('title', models.CharField(help_text='Enter your question or suggestion.', max_length=255, verbose_name='Question')),
                ('body', models.TextField(help_text='Please offer details. Markdown enabled.', null=True, verbose_name='Description', blank=True)),
                ('status', models.CharField(default=b'private', max_length=32, verbose_name='Status', db_index=True, choices=[(b'public', 'Public'), (b'private', 'Private'), (b'internal', 'Internal')])),
                ('locked', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='knowledge.Category', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-added'],
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('lastchanged', models.DateTimeField(auto_now=True)),
                ('alert', models.BooleanField(default=True, help_text='Check this if you want to be alerted when a new response is added.', verbose_name='Alert')),
                ('name', models.CharField(help_text='Enter your first and last name.', max_length=64, null=True, verbose_name='Name', blank=True)),
                ('email', models.EmailField(help_text='Enter a valid email address.', max_length=254, null=True, verbose_name='Email', blank=True)),
                ('body', models.TextField(help_text='Please enter your response. Markdown enabled.', null=True, verbose_name='Response', blank=True)),
                ('status', models.CharField(default=b'inherit', max_length=32, verbose_name='Status', db_index=True, choices=[(b'public', 'Public'), (b'private', 'Private'), (b'internal', 'Internal'), (b'inherit', 'Inherit')])),
                ('accepted', models.BooleanField(default=False)),
                ('question', models.ForeignKey(related_name='responses', to='knowledge.Question')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['added'],
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
    ]
