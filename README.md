# Тестовое задание

## Сборка проекта

`docker build -t task_app .`

## Запуск проекта

`docker tun task_app`

## Запуск тестов

Установка всех библиотек

`pip install -r requirements.txt`

Запуск тестов

`pytest test_app.py`


## ВАЖНО !!!

В файле `benchmark_load.pdf` есть результаты нагрузочных тестов для API.
Тесты проводились на железе i5-4460 + 15gb DDR3. При всех тестах API откликалось на страницу /docs и не висло
