# Python_Task

### Тестовое задание:
```
Написать приложение с использованием Django/Flask на бэкенде и React/Vue/Angular на фронтенде. (на выбор)
Приложение представляет собой динамически обновляемую табличку, 
которая через Websockets слушает новые данные на сервере и отображает их. 
Данные которые должны отображатся в табличке: Сумма ставки, Кол-во ставок на такую сумму

Так же, для проверки работоспособности приложения, нужно добавить формочку для отправки новой ставки на сервер. 
В форме достаточно одного поля со ставкой и кнопки отправить.
Для оформления фронтенда используйте фреймворк Materialize
```

#### I. _Технологии_
> 1. Flask  Version-0.12.2 для API
> 2. Python Version-3.6.4
> 3. SqLite3 Version-3.23.1 для хранения данных


## Для запуска программы:
> 1. `git clone https://github.com/Janik-Tarverdyan/Python_Task.git`
> 2. `cd Python_Task`
> 3. `virtualenv -p /usr/bin/python3 .Task`
> 4. `source .Task/bin/activate`
> 5. `python Task/setup.py install`
> 6. `python Task db init`
> 7. `python Task db migrate`
> 8. `python Task db upgrate`
> 9. `python Task runserver`

## Рекомендации
>**Рекомендую использовать Firefox браузер, это самый лучший браузер для разработчиков и тестировщиков.**
