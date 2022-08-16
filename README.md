этот файл содержит инструкцию для работы с проектом

основные концепции: 

1) проект разрабатывается в среде VScode под Windows
2) основной язык проекта Python 3.10.6
3) проект разарабывается на основе фреймворка Flask

настройка рабочего окружения:

1) cкачиваем актуальную версию vscode с оф.сайта https://code.visualstudio.com/
2) после установки IDE нужно установить интерпретатор питона и плагины в самой среде любым из способов
    - интерпретатор на сайте майкрософта либо в консоли командой install
    - в среде просто в поисковой строке вводим python 
3) далее настроим рабочее окружение(зачем? - читать в интернетах), для этого:
    - сначала нужно глобально разрешить ввполнение исполняющих файлов, для этого:
        - открываем PowerShell от имени админа и вводим команду Set-ExecutionPolicy unrestricted
    - далее в терминале среды разработки создаем рабочее окружение и запускае его
        -python -m venv venv
        -venv\Scripts\activate
        -для отключения окружение использовать обратную команду deactivate


как начать работу с проектом:

1) клонируем репоизиторий и вперед

данный файл будет постоянно актуализироваться и обноваляться по мере появления
новых технологии разраьотки. Как минимум здесь будет язык верстки, БД, и возможно инструменты 
для настройки этого окружения. Работу ведем на своих ветках 
