# автотесты по тестовому заданию
работают на python3 + selenium + pytest в качестве раннера

скриншоты в папке screenshots, при запуске тестов они перезаписываются

## Запуск автотестов под Windows
предусловие - установлен браузер Chrome и соответствующий ему chromedriver добавлен в PATH\
установлены python 3+ и virtualenv

1. Склонировать проект:\
**git clone https://github.com/tsmee/ornament.git**
2. Перейти в папку проекта и создать виртуальное окружение:\
**virtualenv ornament**
3. Активировать виртуальное окружение: \
**ornament\Scripts\activate**
4. Установить необходимые модули:\
**pip install -r requirements.txt**
5. Запустить тесты (из той папки, где они лежат):\
**py.test -v**

## Запуск автотестов под macOS
предусловие - установлен браузер Chrome и соответствующий ему chromedriver добавлен в PATH\
установлены python 3+ и virtualenv

1. Склонировать проект:\
**git clone https://github.com/tsmee/ornament.git**
2. Перейти в папку проекта и создать виртуальное окружение:\
**virtualenv ornament**
3. Активировать виртуальное окружение: \
**source ornament/bin/activate**
4. Установить необходимые модули:\
**pip install -r requirements.txt**
5. Запустить тесты (из той папки, где они лежат):\
**py.test -v**
