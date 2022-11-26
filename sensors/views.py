from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .models import Dht, Water, Bmp

from django.shortcuts import render

def sensors(request):
    import poplib
    import email
    import os
    import psycopg2

    con = psycopg2.connect(
        database="WeatherStation",
        user="WeatherStation",
        password="WeatherStation",
        host="127.0.0.1",
        port="5433"
    )
    cursor = con.cursor()


    class GmailTest(object):
        def __init__(self):
            self.savedir = "sensors/jsonFile"

        def test_save_attach(self):
            #self.connection = poplib.POP3_SSL('pop.gmail.com', 995)
            #self.connection.set_debuglevel(1)
            #self.connection.user("sensorstothedatabase@gmail.com")
            #self.connection.pass_("Sensors123")

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

            # messages processing
            for i in range(emails):

                # return in format: (response, ['line', ...], octets)
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

            # I  exit here instead of pop3lib quit to make sure the message doesn't get removed in gmail
            # import sys
            # sys.exit(0)

    d = GmailTest()
    d.test_save_attach()

    import json, psycopg2
    # read JSON file which is in the next parent folder
    # with open('E:\\Дипломная работа\\json\\jsonFile4.json') as f:
    with open('sensors\\jsonFile\\jsonFile.json') as f:
        json_data = f.read()
        json_obj = json.loads(json_data)

    print(json_obj)

    for section, commands in json_obj.items():
        print(section)
        print('\n'.join(commands))

    Date = json_obj['Date']
    DHTtemp = json_obj['DHT']['Temperature']
    DHThum = json_obj['DHT']['Humidity']
    WaterSensor = json_obj['Water sensor']
    BMPtemp_str = json_obj['BMP']['Temperature']
    BMPpres_str = json_obj['BMP']['Pressure']

    import re
    BMPtemp = re.findall(r'\d*\.\d+|\d+', BMPtemp_str)
    print(' '.join(BMPtemp))

    BMPpres = re.findall(r'\d*\.\d+|\d+', BMPpres_str)
    print(' '.join(BMPpres))

    print('\n'"Получилось:")
    print(Date)
    print(DHTtemp)
    print(DHThum)
    print(WaterSensor)
    print(BMPtemp)
    print(BMPpres)

    import datetime
    date = datetime.datetime.strptime(Date, "%d.%m.%Y %H:%M")  # "Date": "23.03.2020 12:21",
    print(date)
    date_str = (date.strftime("%Y-%m-%d %H:%M:%S"))

    # connect to PostgreSQL
    con = psycopg2.connect(
        database="WeatherStation",
        user="WeatherStation",
        password="WeatherStation",
        host="127.0.0.1",
        port="5433"
    )
    cursor = con.cursor()

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

    if date_str != row_dht:
        cursor.execute("INSERT INTO dht (date, temperature, humidity) VALUES (%s,%s,%s)",
                       (Date, DHTtemp, DHThum))
    else:
        print("одинаковые")

    if date_str != row_w:
        cursor.execute("INSERT INTO water (date, characteristic) VALUES (%s,%s)",
                       (Date, WaterSensor))
    else:
        print('одинаковые')

    if date_str != row_bmp:
        cursor.execute("INSERT INTO bmp (date, temperature, pressure) VALUES (%s,%s,%s)",
                       (Date, ''.join(BMPtemp), ''.join(BMPpres)))
    else:
        print('одинаковые')

    # close the connection to the database.
    con.commit()
    cursor.close()

    # bbs = Dht.objects.all()
    # bbs2 = Water.objects.all()
    # bbs3 = Bmp.objects.all()

    bbs = {'bbs': Dht.objects.all(), 'bbs2': Water.objects.all(), 'bbs3': Bmp.objects.all()}

    return render(request, 'sensors/sensors.html', bbs)

def graph(request):
    import matplotlib.pyplot as plt
    import pandas, psycopg2

    # connect to PostgreSQL
    con = psycopg2.connect(
        database="WeatherStation",
        user="WeatherStation",
        password="WeatherStation",
        host="127.0.0.1",
        port="5433"
    )
    cursor = con.cursor()

    # this is the query we will be making
    query = """ 
        SELECT date, temperature 
        FROM dht; 
        """

    df = pandas.read_sql(query, con, index_col=['date'])
    fig, ax = plt.subplots()
    df.plot(ax=ax)

    # Выводим карту и сохраняем её в формате HTML
    # fig.savefig('E:/Дипломная работа/графики/dht.png')

    # this is the query we will be making
    query2 = """ 
            SELECT date, humidity 
            FROM dht; 
            """

    df = pandas.read_sql(query2, con, index_col=['date'])
    fig2, ax = plt.subplots()
    df.plot(ax=ax)

    # this is the query we will be making
    query3 = """ 
        SELECT date, temperature
        FROM bmp; 
        """

    df = pandas.read_sql(query3, con, index_col=['date'])
    fig3, ax = plt.subplots()
    df.plot(ax=ax)

    # this is the query we will be making
    query4 = """ 
            SELECT date, pressure 
            FROM bmp; 
            """

    df = pandas.read_sql(query4, con, index_col=['date'])
    fig4, ax = plt.subplots()
    df.plot(ax=ax)

    # Выводим карту и сохраняем её в формате HTML
    fig.savefig('sensors/static/graph/dht_temp.png')
    fig2.savefig('sensors/static/graph/dht_hun.png')
    fig3.savefig('sensors/static/graph/bmp_temp.png')
    fig4.savefig('sensors/static/graph/bmp_hun.png')

    import os
    from IPython.display import display, Image

    names = [f for f in os.listdir('sensors/static/graph') if f.endswith('dht_temp.png')]
    names = [f for f in os.listdir('sensors/static/graph') if f.endswith('dht_hun.png')]
    names = [f for f in os.listdir('sensors/static/graph') if f.endswith('bmp_temp.png')]
    names = [f for f in os.listdir('sensors/static/graph') if f.endswith('bmp_hun.png')]

    return render(request, 'sensors/graph.html')