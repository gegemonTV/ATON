<h1>Как запустить сервер на локальной машине?</h1>
<h2>1. Настройка окружения (для Windows)</h2>
Откройте командную строку в папке, в которой находится данный README-файл и введите следующие команды:

```bat
./env/Scripts/activate 
(env)> pip install -r requirements
```
Таким образом вы создадите рабочее окружение и установите Django.

<h2>2. Создание и синтез базы данных</h2>
В данном проекте используется СУБД SQLite3. Чтобы создать файл введите в командную строку следующие команды:

```bat
(env)> python manage.py makemigrations
(env)> python manage.py migrate
```
Данные команды применят изменения в таблице базы данных и создадут файл базы данных `db.sqlite3`.
После создания таблицы и применения миграций используйте следующую команду:

```bat
(env)> python db_init.py
```
Данная команда синтезирует данные на основе имеющихся имен, фамилий и отчеств, перемешанных в случайном порядке, а так же создаст случайные данные на основе модуля `random`.

<h2>3. Запуск локального тестового сервера</h2>

После подготовки базы данных запустите сервер на Django, используя следующую команду:

```bat
(env)> python manage.py runserver
```
Данная команда запустит сервер на локальной машине по адресу <link>http://127.0.0.1:8000/</link>. Перейдите по данному адресу, чтобы проверить результат.