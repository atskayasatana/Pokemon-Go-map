# Карта покемонов

Программа для создания собственной карты с покемонами.

## Запуск

Для работы нужен Python3, Django и библиотеки из файла requirements.txt.

Архив с кодом нужно скачать и распаковать в любую удобную директорию.

Пользовательские настройки: DEBUG и SECRET_KEY для проекта нужно прописать в .env файл:
```Python
DEBUG = # TRUE/FALSE, по умолчанию TRUE
SECRET_KEY = # секретный ключ, можно сгенерировать встроенными функциями Django
```
Запускаем среду выполнения и по необходимости создаем/активируем Django.

Создать окружение:
```
conda create -n имя_окружения python=3.6 anaconda 
```

Активировать окружение:
```
conda activate имя_окружения
```

Переходим в папку проекта и устанавливаем библиотеки из файла requirements.txt

```
pip install -r requiremets.txt
```

Запустим миграцию моделей на локальную машину:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

После этого можно запустить локальный сервер:

```
python manage.py runserver
```

Перед нами появится пустая карта Москвы:

![](https://github.com/atskayasatana/Images/blob/cdbb28c2e636fcd8662b8a76e1ab5c40fa273fba/Moscow_empty_card.png)

## Добавление покемонов на карту

Покемонов и их местоположение на карте удобнее добавлять через админку сайта.

Создадим администратора:
```
python manage.py createsuperuser
```
Заполняем имя пользователя(либо оставляем имя по умолчанию), email, пароль:

![](https://github.com/atskayasatana/Images/blob/7babad4221e8ad1b9027fd5505a001ffad48f5a4/create_super_user.png) 

Если всё в порядке, то появится сообщение: Superuser created successfully.

Запускаем сервер снова:
```
python manage.py runserver
```
Переходим в админку http://127.0.0.1:8000/admin/

В появившемся окне вводим логин и пароль созданного суперпользователя:

![](https://github.com/atskayasatana/Images/blob/07b21ef2c499c5787c363f2a415a0c80f1d21018/django_admin.png)

Админка сайта выглядит так:

![](https://github.com/atskayasatana/Images/blob/07b21ef2c499c5787c363f2a415a0c80f1d21018/django_admin_1.png)

### Pokemon 

 Модель для описания покемона, содержит в себе информацию о каждой особи:
 
 * Название покемона на трёх языках: русское название обязательно, остальные - по желанию
 * Фото покемона - обязательно
 * Описание покемона - обязательно
 * Ссылка на фото - необязательное поле
 * Эволюция покемона(в кого превращается) - необязательное, может оставаться незаполненным, если у покемона нет дальнейшей эволюции.
 
 Информацию о покемонах можно взять отсюда: https://pokemon.fandom.com/
 
 Чтобы добавить информацию, нужно нажать на зеленый крестик справа от слова Pokemons.
 
 Информация о бульбазавре выглядит так:
 
 ![](https://github.com/atskayasatana/Images/blob/e51283a98ae819e8f0c538800a19aeba156acbe6/Bulbasaur_info1.png)
 
 После добавления информации о покемоне, он появится на главной странице, а также получит свою персональную страничку с информацией о себе.
 
 Например, после добавления трёх покемонов главная страница будет выглядеть так:
 
 ![](https://github.com/atskayasatana/Images/blob/c36d8418759825715735c61a142c2a0eae89845b/P_main_w_pokemons.png)
 
 Персональная страница Бульбазавра:

 ![](https://github.com/atskayasatana/Images/blob/c36d8418759825715735c61a142c2a0eae89845b/Bulbasaur_self.png)
 
 После того, как будут добавлены все нужные покемоны можно переходить к заполнению информации об их появлениях и исчезновениях.
 
 ### PokemonEntity
 
 Модель для описания появлений/исчезновений покемона, а также дополнительных опций:
 
 * Широта: обязательное поле - географическая широта координаты появления
 * Долгота: обязательно поле - географическая долгота координаты появления
 * Покемон: обязательное поле - покемон, который появится на карте
 * Время появления: обязательное поле - время появления покемона на карте
 * Время исчезновения: обязательно поле - время исчезновения покемона с карты
 * Уровень, здоровье, сила, защита, выносливость : необязательные поля - дополнительные характеристики покемона
 
 Например, появление Бульбазавра на карте может быть описано так:
 
 ![](https://github.com/atskayasatana/Images/blob/f2f46be8fcdf6cafb0da922ba7f595ce4fab10fc/Bulbasaur_entity.png)
 
 После внесения данных о всех появлениях покемоны появятся на карте:
 
 ![](https://github.com/atskayasatana/Images/blob/d9827cfa6f8a55f697da81ec08279695b3ae4222/P_main_wt_pmons.png)
 
 На странице каждого их покемонов появится на карте можно увидеть положение данного покемона:
 
 ![](https://github.com/atskayasatana/Images/blob/d9827cfa6f8a55f697da81ec08279695b3ae4222/Ivizavr.png)
 
 
 
 
 
 
 
 
 

 
 
 











