# -*- coding: utf-8 -*-


import pandas
import psycopg2

#Connect to an existing data base
conn = psycopg2.connect(dbname="usco1", user="usco1", password="usco1")

#Open a cursor to perform database operations
cur = conn.cursor()

url="https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv?fbclid=IwAR3S0tZfnc3onbg_p5vqHLehMS2VoLs5leCsnCbG1dvPQxf6IbLsBbfEyLw"
df = pandas.read_json(url)

for index, row in df.iterrows():
    sl=row['sl']
    sw=row['sw']
    pl=row['pl']
    pw=row['pw']
    sp=row['species']

    campos = "sepal_lenght, sepal_width, petal_lenght, petal_width, class"
    
    cur.execute("INSERT INTO iris(" + campos +") VALUES(%s, %s, %s, %s, %s)", (sl,sw,pl,pw,sp))

conn.commit()
