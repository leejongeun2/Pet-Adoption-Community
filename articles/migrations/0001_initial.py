# Generated by Django 3.2.13 on 2022-11-30 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('암컷', '암컷'), ('수컷', '수컷')], max_length=20)),
                ('hits', models.IntegerField(default=0)),
                ('breed', models.CharField(choices=[('페르시안', '페르시안'), ('러시안블루', '러시안블루'), ('샴', '샴'), ('렉돌', '렉돌'), ('스코티쉬폴드', '스코티쉬폴드')], max_length=20)),
                ('memo', models.CharField(max_length=20)),
                ('neutered', models.CharField(choices=[('Yes', 'Yes')], max_length=20)),
                ('vaccination', models.CharField(choices=[('Yes', 'Yes')], max_length=20)),
                ('bookmarks', models.ManyToManyField(related_name='catarticle_bookmark', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DogArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('암컷', '암컷'), ('수컷', '수컷')], max_length=20)),
                ('hits', models.IntegerField(default=0)),
                ('breed', models.CharField(choices=[('포메라니안', '포메라니안'), ('웰시코기', '웰시코기'), ('말티즈', '말티즈'), ('시츄', '시츄'), ('푸들', '푸들'), ('비숑', '비숑'), ('시바견', '시바견'), ('골든 리트리버', '골든 리트리버')], max_length=20)),
                ('memo', models.CharField(max_length=20)),
                ('neutered', models.CharField(choices=[('Yes', 'Yes')], max_length=20)),
                ('vaccination', models.CharField(choices=[('Yes', 'Yes')], max_length=20)),
                ('bookmarks', models.ManyToManyField(related_name='dogarticle_bookmark', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DogArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('dogarticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.dogarticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('catarticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.catarticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
