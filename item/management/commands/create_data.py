from django.core.management.base import BaseCommand
from item.models import Item
from faker import Faker

fake = Faker()


# attention! execute the program with the command: >_ python manage.py create_data

class Command(BaseCommand):
    """
    Команда для сброса и добавления тестовых данных в модель Item.

    Метод `handle` выполняет следующие шаги:
    1. Удаляет все записи в модели Item.
    2. Создает 4 элемента.
    """

    def handle(self, *args, **kwargs):
        print("Привет! Начинаю заполнять БД - Wait few minutes!")

        Item.objects.all().delete()

        items = []
        for i in range(4):
            price = fake.pyint(min_value=1000, max_value=30000)
            item = Item.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=price,
            )
            items.append(item)
