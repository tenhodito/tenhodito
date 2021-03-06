# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('camara_deputados', '0006_auto_20170720_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('speeches_count', models.IntegerField(default=0)),
                ('deputies_count', models.IntegerField(default=0)),
                ('proposals_count', models.IntegerField(default=0)),
            ],
            options={
                'get_latest_by': 'datetime',
            },
        ),
        migrations.CreateModel(
            name='Deputy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='camara_deputados.Deputy')),
            ],
            options={
                'ordering': ['data__parliamentary_name', 'data__region'],
            },
        ),
        migrations.CreateModel(
            name='DeputyTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('is_main', models.BooleanField(default=False)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deputytheme_related', to='application.Analysis')),
                ('deputy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='application.Deputy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndexTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('is_main', models.BooleanField(default=False)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indextheme_related', to='application.Analysis')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='application.Deputy')),
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='camara_deputados.Proposal')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indexes', to='application.Proposal')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('is_main', models.BooleanField(default=False)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposaltheme_related', to='application.Analysis')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='application.Proposal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speeches', to='application.Deputy')),
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='camara_deputados.Speech')),
            ],
        ),
        migrations.CreateModel(
            name='SpeechIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('speech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indexes', to='application.Speech')),
            ],
        ),
        migrations.CreateModel(
            name='SpeechTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('is_main', models.BooleanField(default=False)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speechtheme_related', to='application.Analysis')),
                ('speech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='application.Speech')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('initials', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='StateTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('is_main', models.BooleanField(default=False)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statetheme_related', to='application.Analysis')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='application.State')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='statetheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='application.Theme'),
        ),
        migrations.AddField(
            model_name='speechtheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speeches', to='application.Theme'),
        ),
        migrations.AddField(
            model_name='proposaltheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='application.Theme'),
        ),
        migrations.AddField(
            model_name='indextheme',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='application.SpeechIndex'),
        ),
        migrations.AddField(
            model_name='indextheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indexes', to='application.Theme'),
        ),
        migrations.AddField(
            model_name='deputytheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deputies', to='application.Theme'),
        ),
    ]
