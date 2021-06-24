from django.db import models
from django.utils import timezone
from three_be import settings
# Create your models here.



class PostQuerySet(models.QuerySet):

    def published(self):
        return filter(created_at__lte=timezome.now())


class Blog(models.Model):
    title = models.CharField('タイトル', max_length=32)
    thumbnail = models.ImageField('サムネイル', null=True, blank=True)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    objects = PostQuerySet.as_manager()

    def __str__(self):

        return self.title


class Post(models.Model):
    title = models.CharField('タイトル', max_length=32)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    objects = PostQuerySet.as_manager()

    def __str__(self):

        return self.title


class Contact(models.Model):
    first_date = models.DateField('ご希望日（第一希望）', help_text='※')

    first_time = models.DateTimeField('ご希望時間帯（第一希望）', help_text='※')

    second_date = models.DateField('ご希望日（第二希望）', null=True, blank=True)

    second_time = models.DateTimeField(
    'ご希望時間帯（第二希望）', null=True, blank=True,
    help_text='※'
    )

    parent_name = models.CharField(
        '保護者氏名', max_length=50,
        null=True, blank=True, help_text='※'
    )

    student_name = models.CharField('生徒名', max_length=50, help_text='※')

    birthday = models.DateField('生年月日', help_text='※')

    phone_number = models.CharField(
        '電話番号', max_length=12,
        help_text='※',
    )

    email = models.EmailField('メールアドレス', help_text='※')

    text = models.CharField(
        'ご要望・ご質問', max_length=200,
        null=True, blank=True,
    )
    