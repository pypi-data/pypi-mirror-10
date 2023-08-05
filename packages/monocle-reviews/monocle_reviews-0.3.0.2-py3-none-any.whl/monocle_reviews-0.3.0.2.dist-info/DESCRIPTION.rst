---
### Модуль: monocle_reviews
Модуль с отзывами клиентов.
---

## **Пример отображения на сайте:**
![Reviews](/images_readme/reviews.png)

## **Пример отображения в панели администрирования:**
![Reviews](/images_readme/reviews_admin.png)

## **Файл models.py:**

    from django.db import models
    from filebrowser.fields import FileBrowseField

    class Review(models.Model):
        reviewer = models.CharField(max_length=255, verbose_name='Имя клиента')
        image = models.ImageField(upload_to='reviews/%Y/%m/%d', verbose_name='Фото клиента')
        text = models.TextField(verbose_name='Текст отзыва')
        isShown = models.BooleanField(default=True, verbose_name='Показывать отзыв')
        position = models.PositiveIntegerField(default=0, verbose_name='Порядок')

        def __str__(self):
            return self.reviewer

        class Meta:
            verbose_name_plural = u'Отзывы'
            verbose_name = u'Отзыв'
            ordering = ['position']

    from django.apps import AppConfig
    class CustomAppConfig(AppConfig):
            name = 'apps.monocle_reviews'
            verbose_name = 'Отзывы клиентов'

