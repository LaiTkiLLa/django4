from django.db import models


class Scope(models.Model):

    name = models.CharField(max_length=256, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scope = models.ManyToManyField(Scope, through='Scope_Aricle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



class Scope_Aricle(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope_article')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article}_{self.scope}'
