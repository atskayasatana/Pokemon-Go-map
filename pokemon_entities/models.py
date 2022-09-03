from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.TextField(default="", verbose_name="Название покемона")
    title_en = models.TextField(
        blank=True, verbose_name="Название покемона(англ.)"
    )
    title_jp = models.TextField(
        blank=True, verbose_name="Название покемона(яп.)"
    )
    photo = models.ImageField(
        upload_to="media", blank=False, verbose_name="Фото покемона"
    )
    description = models.TextField(
        blank=False, verbose_name="Описание покемона"
    )
    img_url = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Ссылка на фото покемона",
    )
    evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pokemon_evolution",
        verbose_name="Эволюция покемона",
    )

    def __str__(self):
        return "{}".format(self.title)


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name="Широта")
    longtitude = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="Покемон"
    )
    appeared_at = models.DateTimeField(
        default=timezone.now, verbose_name="Время появления"
    )
    disappeared_at = models.DateTimeField(
        default=timezone.now, verbose_name="Время исчезновения"
    )
    level = models.IntegerField(blank=True, default=0, verbose_name="Уровень")
    health = models.IntegerField(
        blank=True, default=0, verbose_name="Здоровье"
    )
    strenght = models.IntegerField(blank=True, default=0, verbose_name="Сила")
    defence = models.IntegerField(blank=True, default=0, verbose_name="Защита")
    stamina = models.IntegerField(
        blank=True, default=0, verbose_name="Выносливость"
    )
