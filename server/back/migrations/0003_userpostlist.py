# Generated by Django 3.2.12 on 2023-03-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.imageupload')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.post')),
            ],
        ),
    ]