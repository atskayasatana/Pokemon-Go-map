import folium

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.timezone import localtime

from .models import PokemonEntity, Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)


def add_pokemon(
    folium_map, lat, lon, description, image_url=DEFAULT_IMAGE_URL
):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    current_time = localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=current_time, disappeared_at__gte=current_time
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longtitude,
            pokemon_entity.pokemon.description,
            pokemon_entity.pokemon.photo.path,
        )

    pokemons_on_page = []

    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append(
            {
                "pokemon_id": pokemon.id,
                "img_url": request.build_absolute_uri(pokemon.photo.url),
                "title_ru": pokemon.title,
            }
        )

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):

    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    
    pokemon_entities = pokemon.entities.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longtitude,
            pokemon_entity.pokemon.description,
            pokemon_entity.pokemon.photo.path,
        )

    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    pokemon.previous_evolution = pokemon.evolutions.first()

    pokemon.next_evolution = pokemon.descendant

    return render(
        request,
        "pokemon.html",
        context={"map": folium_map._repr_html_(), "pokemon": pokemon},
    )
