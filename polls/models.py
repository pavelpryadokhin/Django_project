from django.db import models
from polls import settings
from django.utils.safestring import mark_safe
from django.urls import reverse


class Question(models.Model):
    title = models.CharField('Заголовок', max_length=120)
    timestamp = models.DateTimeField('Дата создания', auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Опубликован')

    def __str__(self):
        return self.title

    def is_popular(self):
        answers = Answer.objects.filter(question_id=self.id)
        votes_total = sum([answer.votes for answer in answers])
        if votes_total > settings.POLLS_POPULAR_VOTES_LIMIT:
            img_path = settings.IMG_TRUE_PATH
        else:
            img_path = settings.IMG_FALSE_PATH
        return mark_safe('<img alt="" src="{}" />'.format(img_path))

    is_popular.short_description = 'Популярный'

    def total_votes(self):
        answers = Answer.objects.filter(question_id=self.id)
        return sum([answer.votes for answer in answers])

    total_votes.short_description = 'Всего голосов'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
