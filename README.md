# Программная часть системы мониторинга 

Программа представляет собой метеорологический сайт, который отображает нынешнюю погоду и прогноз на ближайшие пять дней, а также получает с json файлов данные с датчиков, затем заносит их в базу данных и отображает на сайте в виде таблиц и графиков.

### Установка Django и создание проекта

В данном проекте для работы с Django версии 3.0.5 мы использовали Python 3.6. Устанавливаются все дополнительные пакеты в Python с помощью команды:
```python
PIP (Pip Install Packages)
```

Устанавливается Django точно так же через утилиту PIP, как и большинство библиотек в Python.
После установки проект создался следующей командой: 
```python
Django-admin startprojet WeatherStation
```
Или же если вы используете интегрируемую среду разработку (мы использовали PyCharm), то это можно сделать через панель инструментов.
После чего была создана директория проекта WeatherStation внутри той директории, где мы находились изначально.

    • manage.py – утилита для команды строки, позволяющая взаимодействовать с нашим проектом многими способами
    • weatherstation/__iniy__.py – пустой файл, который указывает Python на то, что данная директория weatherstation является модулем Python.
    • weatherstation/settings.py – конфигурационный файл для данного проекта.  В нем определяется используемая БД, параметры подключения к ней, подключения к проекту приложения и много другое;
    • weatherstation/urls.py – определение URL для данного проекта, то есть содержание будущего сайта;
    • weatherstation/wsgi.py – входная точка для WSGI-совместимых веб-серверов для исполнения нашего проекта.
    
После чего были созданы необходимые приложения, из которых и будет состоять наш сайт. В нашем проекте были созданы два приложения с помощью команды startapp:

```python
Django-admin startapp sensors
Django-admin startapp weatherapp
```

И затем созданные приложения обязательно должны быть подключены к конфигурации файле settings.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weatherapp',
    'sensors',
]
```

Так созданные приложения активны в нашем проекте.

### Создание базы данных и связи с ней

Основой метеорологического сайта являются данные о погоде и данные полученные с датчиков слежения на опасных регионах. Данные нужно будет где-то хранить и обрабатывать, для этого мы использовали базу данных. В Django по умолчанию установлен SQL, но мы уже решили использовать БД PostgreSQL. Для этого следует изначально создать базу данных в консоле или же в кроссплатформенном программном обеспечение (pgAdmin).

Задаем параметры в DATABASE, который находится в settings.py, мы подключаем нашу базу данных «WeatherStation»

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'WeatherStation',
        'USER': 'WeatherStation',
        'PASSWORD': 'WeatherStation',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```


Где:

    • Hоsт - интернет-адрес компьютера, на котором работает СУБД; 
    • PORT - номер ТСР-порта, через который выполняется подключение к СУБД. Значение по умолчанию - пустая строка (используется порт по умолчанию); 
    • USER - имя пользователя, от имени которого Django подключается к базе данных; 
    • PASSWORD - пароль пользователя, от имени которого Django подключается к базе.

И создаем таблицы в models.py:

```python
class Bmp(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bmp'

```

Аналогичным образом создаются модели и для других датчиков слежения, а также городов в папке weatherapp для погоды и ее прогнозирования:
```python
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'

    def __srt__(self):
        return self.name

class Metcast(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Прогноз погоды'
        verbose_name = 'Прогноз погоды'

    def __srt__(self):
        return self.name
```        

Мы используем классы:

    • CharField – обычное строковое поле фиксированной длины. Допустимая длина указывается параметром max_length.
    • FloatField – в этом поле хранятся данных вещественных чисел.
    • DataTimeField – поле для хранятся отметки даты и времени.
    
Мы создали модель данных для датчиков и погоды, далее создали соответствующие таблицы в базе данных. В Django встроена подсистема миграций, которая отслеживает изменения моделей и позволяет транслировать их в базу данных. Команда migrate применяет все миграции для всех приложений из списка INSTALLED_APPS. Она изменяет базу данных с учетом текущих моделей и созданных миграций.

> Миграция - это модуль Python, созданный самим Django на основе определенной модели и предназначенный для формирования в базе данных всех требуемых этой моделью структур: таблиц, полей, индексов, правил и связей. Еще один замечательный инструмент фреймворка, заметно упрощающий жизнь программистам.

Для этого создали инициализирующую миграцию для модели sensors/weatherapp. В корневом каталоге проекта выполнили следующую команду:
```python
Python manage.py makemigrations
```

И Django для нас создала файлы 0001_initial.py в папке migrate приложения sensors/weatherapp:

### Настройка интерфейса для работы с базой данных

Django обеспечивает интерфейс для администрации сайта «из коробки». Нужно его всего лишь настроить, чтобы видеть именно ту информацию, которую требуется. Для этого обратимся к файлу admin.py в приложение sensors/weatherapp:

```python
from django.contrib import admin
from .models import City, Metcast

class CityAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(City, CityAdmin)

class MetcastAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(Metcast, MetcastAdmin)
```

Здесь admin.site.register указывает Django, каким именно модулям нужно обеспечить интерфейс. Также указывается и некоторые дополнительные параметры для отображения:

    • list_display: какие из полей таблицы выводить

Рис.3.10. Настройка свойства отображения

### Создание почтового протокола передачи данных

Для отображения информации на сайте отвечает Views.py. Для того, чтобы скачать, распаковать датчики и построить графики, а также отобразить погоду и прогнозирование, нужно сначала описать все это в файле views.py внутри приложения sensors и weatherapp.
Первым делом мы должны получать данные из датчиков слежения, для этого воспользуемся Gmail почтой. 

Мы написали «мини-клиент», который подключается к серверу и скачивает нужные нам данные. Настраиваемая через административную панель.

Работать с любым почтовым сервисом можно с помощью стандартных почтовых протоколов — это POP3, есть IMAP.
В views приложения sensors устанавливаем специальный модуль poplib и email, которые отвечают за получения писем. 

```python
    class GmailTest(object):
        def __init__(self):
            self.savedir = "sensors/jsonFile"

        def test_save_attach(self):

            cursor.execute("select poplib from settings")
            pop = cursor.fetchone()

            cursor.execute("select user_name from settings")
            user_name = cursor.fetchone()

            cursor.execute("select password from settings")
            password = cursor.fetchone()

            self.connection = poplib.POP3_SSL('pop.gmail.com', 995)
            self.connection.user(user_name)
            self.connection.pass_(password)

            emails, total_bytes = self.connection.stat()
            print("{0} emails in the inbox, {1} bytes total".format(emails, total_bytes))
            # return in format: (response, ['mesg_num octets', ...], octets)
            msg_list = self.connection.list()
            print(msg_list)

            for i in range(emails):

                response = self.connection.retr(i + 1)
                raw_message = response[1]

                str_message = email.message_from_bytes(b'\n'.join(raw_message))

                # save attach
                for part in str_message.walk():
                    print(part.get_content_type())

                    if part.get_content_maintype() == 'multipart':
                        continue

                    if part.get('Content-Disposition') is None:
                        print("no content dispo")
                        continue

                    filename = part.get_filename()
                    if not (filename): filename = "jsonFile.json"
                    print(filename)

                    fp = open(os.path.join(self.savedir, filename), 'wb')
                    fp.write(part.get_payload(decode=1))
                    fp.close


    d = GmailTest()
    d.test_save_attach()
```

### Распаковка json файлов и занесение в БД

Полученные данные в формате json файла мы должны обработать, а именно распаковать и занести нужные таблицы в нашей базе данные. К тому же некоторые данные не соответствовали типу в БД, потому необходимо было менять им тип переменной. 
Для этого мы использовали модуль json, собственно для работы с самими json файлами, и модуль psycopg2, отвечающая за работы с базой данных PostgreSQL.
Затем устанавливаем соединения с БД.

С помощью созданного метода cursor() мы создаем объекты(в нашем случае заносим распакованные json файлы) и через инструкцию INSERT и метод execute() добавляем данные в нужную таблицу. А для того, чтобы в таблицу не были занесены одинаковые данные, и вытаскиваем с базы таблицы последнюю строчку и сверяем ее с той, которую хотим занести по дате.

```python
select_string = "SELECT date FROM dht WHERE ID = (SELECT MAX(ID) FROM dht)"
    cursor.execute(select_string)
    row = cursor.fetchone()
    row_dht = (" ".join(map(str, row)))

    select_string = "SELECT date FROM water WHERE ID = (SELECT MAX(ID) FROM water)"
    cursor.execute(select_string)
    row = cursor.fetchone()
    row_w = (" ".join(map(str, row)))

    select_string = "SELECT date FROM bmp WHERE ID = (SELECT MAX(ID) FROM bmp)"
    cursor.execute(select_string)
    row = cursor.fetchone()
    row_bmp = (" ".join(map(str, row)))
```

### Построение графиков датчиков слежения

И наконец строим наши графики с помощью модуля matplotlib. Сохраняем полученный результат метод savefig объекта Figure, передав ему строку с именем будущего файла и расширения для сохранения.

![](https://raw.githubusercontent.com/aliyakundil/WeatherStation/master/sensors/static/graph/dht.png)

### Создание погодного приложения

И у нас остается еще продемонстрировать текущую погоду и ее ближайший прогноз. Для этого мы воспользовались сайтом OpenWeatherMap, после регистрации получили уникальный API-ключ для того, чтобы получать данные. 


Аналогичным образом пишем код для прогноза на 5 дней, просто меняем URL с текущего, на прогноз.
Мы отправляем запрос на URL, с нужным нам городом, с помощью админ панели, которую мы создали и говорили выше, и получим JSON-нужного нам города. 
Далее нам нужно передать данные в шаблон, чтобы они могли отображаться пользователю.
Мы создаем словарь для хранения всех данных, которые нам нужны. Из данных, возвращаемых нам, нам нужны временные данные, температура и значок текущей погоды.

Теперь, когда у нас есть вся необходимая информация, мы можем передать ее в шаблон. Чтобы передать его в шаблон, мы создали переменную с именем context. Это будет словарь, который позволяет нам использовать его значения внутри шаблона.
А затем в render мы добавим контекст в качестве третьего аргумента.

После необходимо определить URL паттеры для view. Для того, чтобы Django знал, какой URL будет у какого view. Для этого внутри приложения sensors и weatherapp создается по файлу urls.py. Этот файл представляет собой список, где приведено соответствие URL и view-функций.

### Создание HTML-шаблонов

> Django Template Language (DTL) – язык, позволяющий создавать динамический html, изолировать элементы, уменьшать количество одинаковых повторяющихся строк в html-файлах и другое. Он спроектирован с целью описания представления, не программной логики. Язык оперирует тэгами, поведение которых похоже на многие конструкции из программирования.
	
Аналогичным образом были прописаны остальные страницы HTML, а это: текущая погода, прогноз погоды, таблицы и графики. С помощью наследования мы будем отображать их всех в главном HTML шаблоне base:

В результате мы получаем следующий сайт, на главной странице которой расположено фиксированное горизонтальное меню со списком разделов сайта (главная страница, текущая погода-прогноз погоды, таблица, датчики) вверху страницы и горизонтальное меню под динамической картинкой погоды с теми же разделами сайтов. Под ней панель с текущей погодой, которая плавно сменяется друг за другом. Затем идет карта Кыргызской Республики, ниже краткое описание «мониторинга окружающей среды». Ссылки на данные прогнозов погоды, построенных таблиц и графиков. Сайт состоит из пяти разделов, на которые мы переходим по выше описанным ссылкам. 

![главная страница сайта](https://raw.githubusercontent.com/aliyakundil/WeatherStation/master/sensors/static/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20%D1%81%D0%B0%D0%B9%D1%82%D0%B0.png)
