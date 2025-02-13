import sqlite3 as sq
from time_now import time_now


def what_group(les, ID):
    with sq.connect('users.db') as con:
        cur = con.cursor()
        group = cur.execute('SELECT gr FROM users_1 WHERE id = ?', [ID])
    group = group.fetchone()[0]
    res_lesson = []
    for i in les:
        i = str(i)
        if '/' in i:
            ind = i.index('/')
            les1 = [i[:ind],i[ind + 1:]]
            if group in [1,2]:
                h = les1[group-1]
            else:
                h = i
        else:
            h = i
        res_lesson.append(h)
    return res_lesson


def users(DB):
    with sq.connect('users.db') as con:
        cur = con.cursor()
        g = cur.execute('SELECT id FROM users_1 WHERE class = ? and messages = 1', (DB[:-3],))
    g = g.fetchall()
    g = [i[0] for i in g]
    return g


def lesson(DB):
    t = time_now()
    com_time = t[-1]
    day = t[-2]
    with sq.connect(f'{DB}.db') as con:
        cur = con.cursor()
        now_less = cur.execute(f'SELECT {day}.id, {day}.lesson, {day}.teacher, {day}.class FROM {day},time WHERE {day}.id = time.id and time.start <= ? and ? <= '
                               f'time.finish', [com_time, com_time])
        now_less = now_less.fetchall()
        if now_less:
            now_less = now_less[0]
        else:
            now_less = 0
        next_less = cur.execute(f'SELECT {day}.id, {day}.lesson, {day}.teacher, {day}.class FROM {day},time WHERE {day}.id = time.id and time.start > ?', [com_time])
        next_less = next_less.fetchall()
        if next_less:
            next_less = next_less[0]
        else:
            next_less = 0
    return [now_less, next_less]


def get_db(ID):
    with sq.connect('users.db') as con:
        cur = con.cursor()
        user_db = cur.execute('SELECT class FROM users_1 WHERE id = ?', (ID,))
    user_db = user_db.fetchone()[0]
    return user_db

def dbs_1():
    dbs = []
    dbs1 = []
    with sq.connect('users.db') as con:
        cur = con.cursor()
        h = cur.execute('SELECT class FROM groups').fetchall()
    for i in h:
        dbs.append(f'{i[0]}.db')
        dbs1.append(i[0])
    return dbs,dbs1
