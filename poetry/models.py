from django.db import models
from django.contrib.auth.models import User


class Poem(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")
    body = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    likes = models.IntegerField(verbose_name="Лайки")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время публикации"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"
