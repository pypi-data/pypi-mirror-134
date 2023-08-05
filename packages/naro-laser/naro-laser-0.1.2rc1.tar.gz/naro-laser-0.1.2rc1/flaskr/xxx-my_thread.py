import time
from threading import Thread
import schedule


def print2(*s1):
    print('   [' + __name__ + ']', *s1)


def job_time_mark():
    print(f'     ** {time.asctime()}     ', end='\r')


def th2_keyinput():
    # dev.key.bt_sel.when_pressed = menu.button_sel #bt.sel
    # dev.key.bt_inc.when_pressed = menu.button_inc #bt.inc
    # dev.key.bt_dec.when_pressed = menu.button_dec

    while True:
        time.sleep(0.1)  # 100ms
        print('.', end=' ')


def th3_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)



def my_thread_main():
    print2('my_thread_main() start')
    schedule.every(1).seconds.do(job_time_mark)

    th2 = Thread(target=th2_keyinput)
    th2.daemon = True
    th2.start()

    th3 = Thread(target=th3_schedule)
    th3.daemon = True
    th3.start()

