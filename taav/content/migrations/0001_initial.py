# Generated by Django 4.2 on 2024-07-29 09:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatred_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('caption', models.TextField(blank=True, verbose_name='caption')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='location.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatred_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatred_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('media_type', models.PositiveSmallIntegerField(choices=[(1, 'Image'), (2, 'Video')], default=1, verbose_name='media type')),
                ('media_file', models.FileField(upload_to='contenty/media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'mp4', 'wmv', 'flv', 'png'))], verbose_name='media file')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='content.post')),
            ],
            options={
                'verbose_name': 'PostMedia',
                'verbose_name_plural': 'PostsMedia',
            },
        ),
    ]
