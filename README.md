# TeleNah
:heart_eyes: by https://lolz.guru/members/2977610/
----
    Информация
После успешного запуска ждёт пока будет любой пост в каналах (которых аккаунт есть) и если у него открыты комментарии, то отправляет сообщение под этим постом.

    Настройка
> config.json
> - "API_ID": как получить: https://core.telegram.org/api/obtaining_api_id (любого аккканта)
> - "API_HASH": как получить: https://core.telegram.org/api/obtaining_api_id (любого аккканта)
> - "PatchFileText": "имя_файла.txt"  - файл с текстами (1-строчка: 1 текст; 2-строчка: 2 текст и так далее) Форматирование !Markdown! (для переноса строки: "[n]" ): https://core.telegram.org/bots/api#markdownv2-style
> - "PatchFileAccounts": "имя_файла.txt" - файл с номерами аккаунтов теллеграм, на которые нужно заходить
> - "PatchFileChannels": "имя_файла.txt" - файл с данными каналов (Паблик: @usermame; Приват: https://t.me/+QWERTYUIO либо t.me/+QWERTYUIO)
> - "link_preview": false - предпросмотор ссылок (true/false)
> - "token_bot": "1234567890:qwertyuiopQWERTYUIOP" - Токен бота, взять:  https://t.me/BotFather - для отключения, просто: false.
> - "user_id": 1234567890 - id пользователя кому будут приходить лог работы, взять: https://t.me/getmyid_bot - для отключения, просто: false.
-----
    Инструкция по запуску

> Windows:
> - Установить Python 3.9
> - Запустить файл install_libs.cmd
> - Заполнить файл config.json
> - Запустить start.cmd
-----
>Linux (ubuntu и другие на этой платформе)
> - Установить Python 3.9
>> - Запустить install_pyenv.sh
>> - Запустить set_pyenv.sh
> - Запустить install_libs.sh
> - Заполнить файл config.json
> - Запустить start.sh

