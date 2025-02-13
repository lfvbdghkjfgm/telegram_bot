from gets import users, lesson, what_group
from send import send_mess
from check import is_holiday


def send(time1, db):
    user = users(db)
    h = lesson(db[:-3])[1]
    if h:
        for i in user:
            h = what_group(h, i)
            send_mess(i, f'Урок через {time1} минут', 0)
            send_mess(i,
                      f'Сейчас будет урок - {h[1]}\nУчителя зовут {h[2]}\nУрок будет в кабинете {h[3]}', 0)


def not1(already_sent, com_time, next_time, first_time):
    if already_sent != com_time:
        for i in range(len(next_time)):
            if is_holiday(next_time[i][1][:-3]):
                if next_time[i][0] - com_time == 5:
                    send(5, next_time[i][1])
                    already_sent = com_time
                if first_time[i][0] - com_time == 30:
                    send(30, first_time[i][1])
                    already_sent = com_time
    return already_sent
