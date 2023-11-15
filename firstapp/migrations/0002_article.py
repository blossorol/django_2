# Generated by Django 4.2.7 on 2023-11-15 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article_title",
                    models.CharField(max_length=100, verbose_name="文章标题"),
                ),
                ("article_content", models.TextField(default="", verbose_name="正文")),
                (
                    "article_create_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="创建时间"
                    ),
                ),
                (
                    "article_modify_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "article_read_nums",
                    models.IntegerField(default=0, verbose_name="阅读量"),
                ),
                (
                    "article_like_nums",
                    models.IntegerField(default=0, verbose_name="点赞量"),
                ),
            ],
            options={
                "verbose_name": "文章详情",
                "verbose_name_plural": "文章详情",
            },
        ),
    ]