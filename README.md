# Promocode generator
Является ядром проекта

### Технологии
- Django
- Django Rest Framework

### Необходимые зависимости
Установите docker, docker-compose, git.

## Развертывание сервиса (Ubuntu):
Склонируйте проект из github. 
```sh
https://github.com/tinkml/goodbit.git
```
Зайдите в папку с проектом.
```sh
cd goodbit/promocode_generator/
```

### 1. Запуск Веб-приложения:
1.1. Скопируйте из *.env.example в .env, указав необходимые переменные.

1.2. Вернитесь в корневую папку goodbit/:
```sh
cd ..
```
1.3. Запустите процесс сбоки контейнеров с помощью docker-compose.
```sh
docker-compose up -d --build
```
1.4. После сборки контейнеров, адрес backend-сервера.
```sh
http://0.0.0.0:8000/
```
1.5. Документация по API backend будет находиться по адресу.
```sh
http://0.0.0.0:8000/swagger/
```

### 2. Подготовка приложения для работы через консоль.
2.1. Установите переменные окружения из *.env.example в среду, где будет запускаться приложение.

2.2. После установки переменных, будут достпны следующие команды через стандартный скрипт Django:
```sh 
# параметр "-h" - подробная информация о команде
python3 manage.py add_promo_codes # Добавление группы промо кодов
python3 manage.py срусл_promo_code # Проверка наличия промо кода по названию
```

### Полезные ссылки
- Docker - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10
- Docker-compose - https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-debian-10-ru
- Git - https://timeweb.com/ru/community/articles/kak-ustanovit-git-na-debian-10-1
