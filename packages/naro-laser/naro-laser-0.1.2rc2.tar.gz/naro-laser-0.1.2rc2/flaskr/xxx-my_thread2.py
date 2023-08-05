import logging
import threading
import time
import socket
import copy
from .naro_timer import naro_timer
from flaskr.hw import adc
from flaskr.hw import lcd
from flaskr.hw import mcp23_simple


logging.warning('=========================')
logging.warning('importing my_thread2')
logging.warning('=========================')


def job_time_mark():
    print(f'     ** {time.asctime()}     ', end='\r')


def th_func1(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


# def th_func3_ads(arg1):
#     for i in range(5):
#         # print(i)
#         lg.debug(f'th_func3:#{i}')
#
#         time.sleep(1)


# lg = logging.getLogger('myThread')


# def set_logger_1():
#     global lg
#
#     # lg.setLevel(logging.DEBUG - 1)
#     lg.setLevel(logging.INFO)
#
#     # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     formatter = logging.Formatter('  <%(name)s> %(levelname)s:%(message)s')
#     stream_handler = logging.StreamHandler()
#     stream_handler.setFormatter(formatter)
#     lg.addHandler(stream_handler)
#     file_handler = logging.FileHandler('log12-' + socket.gethostname() + '-my.log')
#     lg.addHandler(file_handler)
#     lg.propagate = 0  # 부모 로거에게 전파하지 마라
#
#
#     lg.warning('---------------------')
#     lg.warning('log start')
#     lg.warning(time.asctime())
#     lg.warning('---------------------')
#
#     # lg.critical('*** logging test msg')
#     # lg.error('*** logging test msg')
#     # lg.warning('*** logging test msg')
#     # lg.info('*** logging test msg')
#     # lg.debug('*** logging test msg')


def main():
    # set_logger_1()  # for data

    logging.debug('main(), start logger')

    def th_func2_adc_max(arg1):
        """ADC 최대 샘플링 속도를 측정한다"""
        t1 = naro_timer.Timer()
        t1.diff()
        t1.diff()
        for i in range(5):  # 스레드에서 실행되는 이 함수는 이걸로 끝난다.
            list1 = []
            list2 = []
            a = 0
            for j in range(3200):
                list1.append(adc.ad1.read())

            t1.check()
            time.sleep(0.9)

    def th_func2(arg1):
        """ADC read 데이터를 다른 함수에서 사용가능하게 한다"""
        # global lg
        # t1 = naro_timer.Timer()
        # lg.debug(t1.diff())
        # lg.debug(t1.diff())
        i = 0
        # global lg   # for data log
        while True:
            i += 1
            a = 0
            lst_time = []
            lst_data = []
            for j in range(4):
                lst_data.append(adc.ad1.read())
                lst_time.append(time.time())    # 이게 아래보다 낫다
                pass

            logging.warning(lst_time)  # 현재 파일에도 가록한다 21.09
            logging.warning(lst_data)
            lcd.disp.pr(hex(i))
            time.sleep(2)

    # th = threading.Thread(target=th_func2_adc_max, args=(1,))
    th = threading.Thread(target=th_func2, args=(1,))
    th.daemon = True  # 거친 방법인데...
    th.start()
    # th.join() # 세련된 방법
    '''위 두가지 모두 무한루프 쓰레드를 종료시키지 못하는 듯 21.08
    해결:
        데몬 설정이 먹힌다 그런데 start() 전에 설정하니 성공
    '''
    logging.debug('main() end')
