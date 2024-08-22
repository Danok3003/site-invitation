from django.db import models

class Guest(models.Model):

    name_first_guest = models.CharField(max_length=30, verbose_name='Имя первого гостя')
    name_second_guest = models.CharField(max_length=30, verbose_name='Имя второго гостя', blank=True)
    name_slug = models.SlugField(max_length=30, blank=True, unique=True)

    first_seconds_names = models.CharField(max_length=200, verbose_name='Имена+Фамилии', blank=True)

    one_plus = models.BooleanField(verbose_name='+1 гость', blank=True, default=False)

    drinks = models.CharField(max_length=1000, verbose_name='Напитки', blank=True)

    presence_on_wedding = models.BooleanField(verbose_name='Присутствие на свадьбе', blank=True)

    class Meta:

        ordering = ["name_first_guest"]
        verbose_name = 'Свадьба'
        verbose_name_plural = 'Свадьба'

    def __str__(self):
        return self.name_first_guest + ' и ' + self.name_second_guest

    def get_absolute_url(self):
        pass

class Timer(models.Model):
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    class Meta:

        verbose_name = 'Дата свадьбы'
        verbose_name_plural = 'Дата свадьбы'

    def __str__(self):
        return 'Время события'