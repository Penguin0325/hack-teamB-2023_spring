# Generated by Django 3.2.12 on 2023-03-15 12:50

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
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('loginID', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('createDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
                ('deleteDate', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('createDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
                ('deleteDate', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
