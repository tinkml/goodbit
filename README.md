# Promocode generator
Является ядром проекта

## Технологии
- Django
- Django Rest Framework

### Необходимые зависимости
Установите docker, docker-compose, git.

### Развертывание сервиса (Ubuntu)
Склонируйте проект из github. 
```sh
https://github.com/tinkml/goodbit.git
```
Зайдите в папку с проектом.
```sh
cd goodbit/promocode_generator/
```
Скопируйте из *.env.example в .env, указав необходимые переменные.

Вернитесь в корневую папку goodbit/:
```sh
cd ..
```
Запустите процесс сбоки контейнеров с помощью docker-compose.
```sh
docker-compose up -d --build
```
После сборки контейнеров, откройте браузер и зайдите по адресу.
```sh
0.0.0.0:8000
```

### Полезные ссылки
- Docker - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10
- Docker-compose - https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-debian-10-ru
- Git - https://timeweb.com/ru/community/articles/kak-ustanovit-git-na-debian-10-1
