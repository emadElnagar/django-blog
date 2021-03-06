# Generated by Django 3.1.7 on 2021-05-11 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_like_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replied_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-replied_at'],
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_liked',
        ),
        migrations.DeleteModel(
            name='Like_comments',
        ),
        migrations.AddField(
            model_name='replycomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='blog.comment'),
        ),
        migrations.AddField(
            model_name='replycomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
