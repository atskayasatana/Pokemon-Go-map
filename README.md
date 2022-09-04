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






