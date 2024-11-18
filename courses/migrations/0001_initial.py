# Generated by Django 5.1.3 on 2024-11-18 07:15

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Publish', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='draft', max_length=50)),
                ('access', models.CharField(choices=[('any', 'Anyone'), ('email_required', 'Email_Required')], default='email_required', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=courses.models.handle_upload)),
            ],
        ),
    ]
