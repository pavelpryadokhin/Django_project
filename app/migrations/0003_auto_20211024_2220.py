# Generated by Django 3.2.8 on 2021-10-24 19:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211024_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('r1', 'Роман'), ('p', 'Поэма'), ('r2', 'Рассказ'), ('s', 'Стих')], default='r1', max_length=2, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
                ('timepublish', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата пуликации')),
                ('active', models.BooleanField(default=True)),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.post', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'comments',
            },
        ),
    ]
