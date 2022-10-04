from django.db import models


class PetrolStore(models.Model):
    coordinate = models.CharField(max_length=20,
                                  verbose_name='Координаты')
    number = models.IntegerField(verbose_name='Номер')
    address = models.TextField(verbose_name='Адрес')

    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'Список АЗС'

    def __str__(self):
        return f'{self.number} - {self.address}'


class Image(models.Model):
    petrol_station = models.ForeignKey('PetrolStore',
                                       on_delete=models.CASCADE,
                                       related_name='images',
                                       verbose_name='АЗС')
    file = models.ImageField(upload_to='logos')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Список изображений'


class Service(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название услуги')
    petrols = models.ManyToManyField('PetrolStore',
                                     blank=True,
                                     related_name='services',
                                     verbose_name='АЗС')
    image = models.ImageField(upload_to='logos',
                              blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Дополнительные услуги'
        verbose_name_plural = 'Список дополнительных услуг'

    def __str__(self):
        return self.name


class Price(models.Model):
    petrol_station = models.ForeignKey('PetrolStore',
                                       on_delete=models.CASCADE,
                                       related_name='prices',
                                       verbose_name='АЗС')
    name = models.CharField(max_length=20,
                            verbose_name='Название топлива')
    cost = models.PositiveIntegerField(verbose_name='Цена топлива')
    currency = models.CharField(max_length=10,
                                verbose_name='Валюта')
    image = models.ImageField(upload_to='logos',
                              blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Список цен'

    def __str__(self):
        return f'{self.name}'
