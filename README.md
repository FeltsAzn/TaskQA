# Основное задание

Для запуска скрипта нужно сделать следующее:
Установить библиотеку cryptography для правильного запуска скрипта из терминала:

> pip install cryptography

(так же, возможно, нужно поставить библиотеку click)

Заходим в папку со скриптом и помещаем свои данные в папку со скриптом (скрипт будет искать файлы относительно папки
самого скрипта).

Открываем терминал в папке скрипта и пишем:

> python ecdsa_digital_signature.py --f <Исходный файл> --s <Цифровая подпись файла> --k <Публичный ключ>


Так же можно написать:
> python ecdsa_digital_signature.py

>> ... Filename: <Исходный файл>

>> ... Signature: <Цифровая подпись файла>

>> ... Key: <Публичный ключ>

Примечание: в папке "task" лежат тестовые данные. Чтобы их использовать нужно перед названием файла писать "task/",
так как скрипт будет пытаться найти файлы в своей папке нахождения.

## Дополнительное задание

Для запуска web приложения на FastAPI заходим в файл fastapi_app и стартуем файл start_app.py
(для простого запуска лучшего всего открыть IDE и установить через pip файл requirements.txt)

После запуска файла start_app.py в строку вывода выйдет информация:

>INFO:     Will watch for changes in these directories: ['<Полный путь месторасположения приложения>']
>INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
>INFO:     Started reloader process [14854] using StatReload
>INFO:     Started server process [14856]
>INFO:     Waiting for application startup.
>INFO:     Application startup complete.

Далее переходим в браузер и открываем http://127.0.0.1:8000/docs для удобного взаимодействия с API сервиса.

### Главная страница
![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/main_page.png)


### Endpoint для подписи файла цифровой подписью

Нажимаете "Try"

Загружаете файл, который хотите подписать


![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/sign.png)




### Ответ сервера

Cкачиваете цифровую подпись этого файла на компьютер (нажать Download file)

![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/sign_response.png)


### Проверка цифровой подписи

Для проверки вашего файла и цифровой подписи на валидность нужно отправить исходный файл и его цифровую подпись (которую вы скачали с метода /sign).

!!! ВАЖНО: сначала загружается исходный файл, только потом цифровая подпись (так же стоит ограничение в 2 файла, чтобы происходила корректная проверка) 

![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/verify.png)

### Ответ сервера

Получаете информацию о валидности вашего файла и его цифровой подписи в ответе {resposne: ANSWER}

![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/verify_response.png)

