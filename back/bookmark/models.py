from django.db import models
from django.db.models.expressions import OrderBy

# Create your models here.


class SecondBookmarkManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(title='naver')


class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    object = models.Manager()
    second_objects = SecondBookmarkManager()
    # 객체를 문자열로 표현할 때 사용
    # Admin 등에서 사용됨

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        db_table = 'bookmark'
        verbose_name = "my faveorite Name"
        verbose_name_plural = "my faveorite Names"


class Album(models.Model):
    name = models.CharField('NAME', max_length=30)
    description = models.CharField(
        'On Line Description', max_length=100, blank=True)
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)


class Publication(models.Model):
    title = models.CharField(max_length=30)
    albums = models.ManyToManyField(Album)
