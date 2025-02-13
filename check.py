import sqlite3 as sq
from time_now import time_now


def is_id(ID):
    with sq.connect('users.db') as con:
        cur = con.cursor()
        ids = cur.execute('SELECT id FROM users_1')
    ids = ids.fetchall()
    ids = [i[0] for i in ids]
    if ID in ids:
        return True
    else:
        return False


def is_holiday(DB):
    t = time_now()
    month = t[0]
    day = t[1]
    week = t[2]
    if week in ['saturday', 'sunday']:
        return False
    with sq.connect(f'{DB}.db') as con:
        cur = con.cursor()
        days = cur.execute('SELECT days FROM holidays WHERE month = ?', (month,))
    days = days.fetchone()[0].split()
    if str(day) in days:
        return False
    else:
        return True
