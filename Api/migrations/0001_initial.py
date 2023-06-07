# Generated by Django 3.2.19 on 2023-06-01 10:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('impact', models.BigIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('ease', models.BigIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('confidence', models.BigIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('is_done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]