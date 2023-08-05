---
### Модуль: monocle_menu
---

Меню для навигации по сайту. Переходы между блоками анимированы.

## **Пример отображения на сайте:**
![Menu](/images_readme/menu.png)

## **Пример отображения в панели администрирования:**
![Menu](/images_readme/menu_admin1.png)

![Menu](/images_readme/menu_admin2.png)

## **Файл models.py:**

    from django.db import models

    class Menu(models.Model):
        name = models.CharField(max_length=255, verbose_name='Название пункта меню')
        anchor = models.CharField(max_length=255, verbose_name='ID блока')
        position = models.PositiveIntegerField(default=0, verbose_name='Позиция')

        def __str__(self):
            return self.name

        class Meta:
            verbose_name_plural = u'Меню'
            verbose_name = u'Элемент меню'
            ordering = ['position']




