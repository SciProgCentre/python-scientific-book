# Установка Python и ПО

![png](https://imgs.xkcd.com/comics/python_environment.png)

Для того что бы начать работать с Python нужно установить его, а также некоторые полезные инструменты. Существуют несколько вариантов как работать с Python, здесь мы изложим два самых доступных, об остальных вариантах вы можете узнать в расширенном руководстве.

## Дистрибутив Anaconda

[Дистрибутив](https://ru.wikipedia.org/wiki/Дистрибутив) Anaconda содержит в себе все необходимое для работу с Python:

* Около тысячи пакетов для языков программирования Python и R;
* Может быть установлен на любой популярной операционной системе (Windows, Linux и MacOS)
* Использует пакетный менеджер `conda` и предоставляет графический интерфейс для него;
* Рабочая тетрадь [Jupyter Notebook](https://jupyter.org)
* Рабочее окружение `Anaconda Navigator`
  
## Установка дистрибутива Anaconda

Для загрузки перейдите на сайт [anaconda.com](https://www.anaconda.com/), нажмите кнопку `Downloads` в правом верхнем углу страницы, выберите свою операционную систему (Windows, MacOS или Linux)

### Windows

Нажмите кнопку `64-Bit Graphical Installer` или `32-Bit Graphical Installer` под надписью `Python 3.7` в зависимости от разрядности системы (разрядность можно узнать [вот так](https://support.microsoft.com/ru-ru/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) или [так](https://support.microsoft.com/ru-ru/help/15056/windows-32-64-bit-faq)). Запустите скачанный файл и следуйте инструкции. После установки программы из Anaconda будут доступны в меню `Пуск`, для управления Anaconda вы можете использовать программу `Anaconda Navigator`.

### MacOs

Нажмите кнопку `64-Bit Graphical Installer` под надписью `Python 3.7`, запустите скачанный файл и следуйте инструкции.

### Linux

Нажмите кнопку `64-Bit (x86) Installer` под надписью `Python 3.7`. Откройте терминал и перейдите в папку где лежит скачанный файл:

```bash
cd путь/до/директории/c/файлом
```

После чего разрешите исполнение скачанного файла (имя файла может отличаться):

```bash
chmod +x Anaconda3-5.1.0-Linux-x86_64.sh
```

и запустите установку:

```bash
./Anaconda3-5.1.0-Linux-x86_64.sh
```

следуйте инструкции.

## Google Colab

Также есть возможность не устанавливать дистрибутив `Anaconda`, а пользоваться [`Google Colab`](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true) (документация есть на официальном сайте).
