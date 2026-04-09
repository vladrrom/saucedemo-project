# SauceDemo Login Test Project

Проект содержит набор автоматизированных тестов для сайта [SauceDemo](https://www.saucedemo.com/). Реализовано 5 автотестов на Python с использованием Selenium, Pytest, Allure и паттерна Page Object.  

## Покрываемые сценарии

- успешный логин `standard_user / secret_sauce`
- логин с неверным паролем
- логин заблокированного пользователя `locked_out_user`
- логин с пустыми полями
- логин пользователем `performance_glitch_user` (проверка корректного перехода и проверка открытия страницы несмотря на возможные задержки)

## Используемый стек

- Python 3.10
- Selenium
- Page Object
- Allure
- Pytest
- Docker

## Структура проекта

- `tests/` — тесты
- `pages/` — Page Object классы
- `utils/` — тестовые данные и локаторы
- `conftest.py` — фикстуры и hooks
- `requirements.txt` — зависимости
- `Dockerfile` — запуск тестов в контейнере

## Установка зависимостей

```
pip install -r requirements.txt
```

## Локальный запуск
```
pytest
```

## Запуск через Docker
```
docker build -t saucedemo-tests .
docker run --rm -v "/$(pwd)/allure-results:/app/allure-results" saucedemo-tests
```

## Allure Report
Для просмотра Allure-отчёта:
```
allure serve allure-results
```