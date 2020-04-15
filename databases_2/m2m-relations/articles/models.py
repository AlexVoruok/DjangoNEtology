from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tags, through='TagRelation', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class TagRelation(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    main_tag = models.BooleanField()

    class Meta:
        ordering = ['tags', ]
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

