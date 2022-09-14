from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    title_en = models.CharField(max_length=200,
                                blank=True,
                                verbose_name="Название покемона(англ.)"
                                )
    title_jp = models.CharField(max_length=200,
                                blank=True,
                                verbose_name="Название покемона(яп.)"
                                )
    photo = models.ImageField(upload_to="media/",
                              blank=True,
                              verbose_name="Фото покемона"
                              )
    description = models.TextField(blank=True,
                                   verbose_name="Описание покемона"
                                    )
    descendant = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="evolutions",
        related_query_name="evolution",
        verbose_name="Эволюция покемона",
        )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name="Широта")
    longtitude = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(
                                Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name="Покемон",
                                related_name='entities'
                                 )
    appeared_at = models.DateTimeField(
                                       default=timezone.now,
                                       verbose_name="Время появления"
                                      )
    disappeared_at = models.DateTimeField(
                                          default=timezone.now,
                                          verbose_name="Время исчезновения"
                                          )
    level = models.IntegerField(blank=True, verbose_name="Уровень")
    health = models.IntegerField(null=True,
                                 blank=True,
                                 verbose_name="Здоровье"
                                 )
    strength = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
    stamina = models.IntegerField(null=True,
                                  blank=True,
                                  verbose_name="Выносливость"
                                  )
