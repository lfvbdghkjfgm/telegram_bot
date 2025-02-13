import sqlite3 as sq
from time_now import time_now


def first(dbs):
    first_time = []
    for i in dbs:
        with sq.connect(i) as con:
            cur = con.cursor()
            h = cur.execute('''SELECT start FROM time WHERE id = 1''')
        h = h.fetchone()
        first_time.append([h[0], '157610Г.db'])
    return first_time


def next_les(dbs):
    next_time = []
    for i in dbs:
        with sq.connect(i) as con:
            cur = con.cursor()
            h = cur.execute('''SELECT start FROM time WHERE start>?''', (time_now()[-1],))
            h = h.fetchall()
            if len(h):
                next_time.append([h[0][0], '157610Г.db'])
            else:
                next_time.append([0, '157610Г.db'])
    return next_time
