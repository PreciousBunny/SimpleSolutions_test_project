from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    """
    Класс описания модели Item.
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.PositiveIntegerField(default=1000, verbose_name='Стоимость')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
