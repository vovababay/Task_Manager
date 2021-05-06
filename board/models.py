from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name="Название", db_index=True)
    content = models.TextField(blank=True, verbose_name="Описание")
    date_created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалено")
    column = models.ForeignKey("Column", on_delete=models.PROTECT, verbose_name="Колонка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
        ordering = ["date_created"]


class Column(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название", db_index=True)
    date_created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Колонка"
        verbose_name_plural = "Колонки"
        ordering = ["date_created"]
