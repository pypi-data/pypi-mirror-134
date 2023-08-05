# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

"""
`ModuleName`
====================================================

module for the ...

* Author(s): NaSeokhwan (2021)
"""

import sys
import logging
import socket
import threading
import time
import json
import statistics
import requests
import naro

print('<-', __name__)

from flaskr import my_globals as gm
from flaskr import __about__
from flaskr.hw import adc
from flaskr.hw import lcd
from flaskr.hw import cpu
from flaskr.hw import uart
from flaskr.hw import bme280
from flaskr.hw import ledcolor as led

print(__about__.__title__, __about__.__version__, __about__.__build_date__)
print(__about__.__summary__)


# # 외부 파일 참조
# if sys.platform == 'win32':
#     sys.path.append('e://bb//python//serial-com')
# elif sys.platform == 'linux':
#     sys.path.append('/home/pi/mnt/python/serial-com')
# from wdn400s import ModemMqtt

from flaskr.hw.wdn400s import ModemMqtt

# 기본 로거 설정
mylog = logging.getLogger('mylog')

# 주변장치 존재 여부
gm.peri['adc'] = adc.ad1.attached
gm.peri['lcd1'] = lcd.disp1.attached
gm.peri['bme280'] = bme280.bme280.attached

# ThingsBoard server sample: 'http://nash.wo.tc:9090/api/v1/RASPBERRY_PI_DEMO_TOKEN/telemetry'
things_cred = socket.gethostname().lower()  # 'RPI-LASER01'

if 1:
    # things_sv1 = 'http://nash.wo.tc:9090/api/v1/'  # 내 사이트, 21.1211부터 종료함
    things_sv1 = 'http://nash.mywire.org:9090/api/v1/'  # 내 사이트
    things1 = things_sv1 + things_cred + '/telemetry'

if 0:
    things_sv2 = 'https://demo.thingsboard.io/api/v1/'  # 온라인 데모 사이트
    things2 = things_sv2 + things_cred + '/telemetry'

things_headers = {
    'Content-type': 'application/json',
}


def list_diff(lst):
    diff = []
    p_x = 0
    for x in lst:
        us = int((x - p_x) * 1000 * 1000)  # micro second
        diff.append(us)
        p_x = x
    diff[0] = 0
    return diff


def config_from_to_file(cmd):
    """앱 설정을 파일에 쓰거나 불러오기"""
    dic = gm.cnfg
    # print(__name__, 'dic:', dic)
    # lg.info(f'gm.cnfg: {gm.cnfg}')

    # dic --> json
    jo = json.dumps(dic, ensure_ascii=True)  # 한글금지
    # print(__name__, 'json:', jo)

    conf_filename = 'config_app.json'

    if cmd is 'save':
        # 'wt' 를 사용하면 더러워진다 그리고 숫자를 스트링 처리한다
        with open(conf_filename, 'w') as f:  # with: 파일닫기를 자동으로
            # json --> file
            json.dump(jo, f)  # indent 안먹힌다
            print(__name__, 'save config to file:', jo)

    if cmd is 'load':
        try:
            with open(conf_filename, 'r') as f:
                # file --> json
                jo = json.load(f)
                # print(__name__, 'load config from file:', jo)
                mylog.info('load config from file:' + str(jo))

                # json --> python dic
                dic = json.loads(jo)
                gm.cnfg = dic
                print(__name__, 'config file found')
                print(__name__, 'default global config values will be replaced!!!')
        except:
            print('no config file found')


# if True:
def create_threads():
    """create ny threads"""

    print(__name__, 'fun:create_threads() start')
    print(__name__, socket.gethostname() + ', ' + time.asctime())

    if True:    # config structure changed, 개발시, 첫 배치에는 항상 이걸로 하라.
        config_from_to_file(cmd='save')
    else:       # 배치 후 테스트 완료 후 이 모드를 사용해야 한다.
        config_from_to_file(cmd='load')
        gm.cnfg['from_file'] = True

    def th_func2(arg1):
        """ADC read 데이터를 다른 함수에서 사용가능하게 한다"""
        # print('fun_2')
        lg = logging.getLogger('th_func2')
        lg.propagate = 0
        lg.setLevel(logging.DEBUG)
        lg.critical('---')
        lg.info(time.asctime())
        lg.info(gm.cnfg)

        t1 = naro.Timer()
        t1.clear()

        # print('\n\n=======Test===', gm.cnfg)
        # print('\n\n=======Test===', gm.lte2)

        cnt = 0
        while True:
            cnt += 1
            lst_time = []
            lst_data = []
            size = gm.cnfg['sample']['size']
            period = float(gm.cnfg['sample']['period']) / 1000  # ms -> second
            MIN_PERIOD_ADS = 1 / 3300  # for ADS1015. 0.303ms
            MIN_PERIOD = 1 / 4000
            decimation = int(period / MIN_PERIOD)
            assert decimation >= 1
            gm.status['sample']['decimation'] = decimation

            if cnt < gm.max_log:
                lg.info(f'cnt: {cnt}, decimation: {decimation}')
                if period < MIN_PERIOD_ADS:
                    lg.info('sampling period setting is too low. 0.33ms will be used instead.')

            if period < 1.0 / 1000:  # high speed, Decimation, 모두 이걸로 테스트
                gm.status['sample']['mode'] = 'Decimation'
                gm.status['sample']['delay'] = None
                for j in range(size * decimation):
                    distance = adc.ad1.read()
                    now = time.time()
                    if j % decimation == 0:
                        lst_data.append(distance)
                        lst_time.append(now)
                        # print('adc capture: ', j, lst_data)
            elif period < 10.0 / 1000:  # mid speed, Delay
                gm.status['sample']['mode'] = 'Delay'
                gm.status['sample']['decimation'] = None
                gm.status['sample']['delay'] = period - 0.20 / 1000  # for mid speed
                for j in range(size):
                    '''대책없이 기다린다. 현재로는 이게 가장 낫다.'''
                    t1.delay_sec(gm.status['sample']['delay'])
                    distance = adc.ad1.read()
                    now = time.time()
                    lst_data.append(distance)
                    lst_time.append(now)
                pass
            else:  # low speed, 이 경우는 현재 없다
                assert period < 10.0 / 1000

                for j in range(size):
                    time.sleep(period)
                    distance = adc.ad1.read()
                    now = time.time()
                    lst_data.append(distance)
                    lst_time.append(now)
                pass

            # 데이터 필터링

            gm.adc_data_mean = statistics.mean(lst_data)
            lst_time_diff = list_diff(lst_time)

            # 로그 파일에 기록

            if cnt < gm.max_log:
                lg.info(lst_time)
                lg.info(lst_time_diff)
                lg.info(lst_data)
                tmp = gm.adc_data_mean
                lg.info(f'adc data_mean: {tmp}')

                # 임시 콘솔에 표시
                # print(__name__, 'ADC:', lst_data)
                # print(__name__, 'TimeDiff:', lst_time_diff)
            elif cnt == gm.max_log:
                lg.info('log count reached max_log(fun2)')
            else:
                pass

            # 웹서버를 위한 데이터 복사 일단 no deep copy
            # print('gm.adc.data, lst_data:', gm.adc_data, lst_data)
            gm.adc_time = lst_time
            gm.adc_data = lst_data
            gm.adc_time_diff = lst_time_diff

            # ThingsBoard
            if cnt % 5 == 0:
                gm.tele1_main['displacement'] = gm.adc_data_mean
                data = json.dumps(gm.tele1_main)

                try:
                    response = requests.post(things1, headers=things_headers, data=data)
                except:
                    lg.error('network error(fun2), Thingsboard server')
                    pass

                # print(things1)

            time.sleep(0.2)  # 200ms:
            # time.sleep(5)     # 초당 5~10 회가 적당

    # th = threading.Thread(target=th_func2_adc_max, args=(1,))
    th = threading.Thread(target=th_func2, daemon=True, args=(1,))
    th.start()
    # th.join() # 세련된 방법
    '''위 두가지 모두 무한루프 쓰레드를 종료시키지 못하는 듯 21.08
    해결:
        데몬 설정이 먹힌다 그런데 start() 전에 설정하니 성공
    '''

    def th_fun3_100ms(arg1):
        cnt = 0
        while True:
            cnt += 1
            if cnt < gm.max_log:
                pass
            elif cnt == gm.max_log:
                pass
            else:
                pass
            time.sleep(0.1)
            pass

    th3 = threading.Thread(target=th_fun3_100ms, daemon=True, args=(2,))
    th3.start()

    def th_fun4_cpu_temp(arg1):
        cnt = 0
        while True:
            cnt += 1
            gm.status['cpu_temp'] = cpu.cpu.get_cpu_temp()

            # if cnt < gm.max_log:
            #     mylog.debug('cpu temp: ' + str(gm.status['cpu_temp']))
            # elif cnt == gm.max_log:
            #     mylog.debug('log count reached max_log(fun4)')
            #     mylog.debug(str(gm.peri))
            # else:
            #     pass

            time.sleep(2)

    th4 = threading.Thread(target=th_fun4_cpu_temp, daemon=True, args=(2,))
    th4.start()

    def th_fun5_lcd(arg1):
        time_fmt = '%m%d,%H:%M:%S'
        s22 = time.strftime(time_fmt, time.localtime(time.time()))
        lcd.disp1.set_cursor(0, 0)
        lcd.disp1.print(s22)

        cnt = 0
        while True:
            cnt += 1
            lcd.disp1.set_cursor(0, 16 * 1)
            lcd.disp1.print(f'[{cnt}]')
            time.sleep(1.0)

    th5 = threading.Thread(target=th_fun5_lcd, daemon=True, args=(2,))
    th5.start()

    def th_fun6_serial(arg1):
        cnt = 0
        while True:
            cnt += 1
            time.sleep(0.5)
            pass

    th6 = threading.Thread(target=th_fun6_serial, daemon=True, args=(2,))
    th6.start()

    def th_fun7_bme280(arg1):
        time.sleep(2)
        cnt = 0
        while True:
            gm.env['temp'] = bme280.bme280.measure_temp()  # Rpi OS 21.10 에서는 라이브러리 버그,
            gm.env['humi'] = bme280.bme280.measure_humi()
            gm.env['pres'] = bme280.bme280.measure_pres()
            gm.env['alti'] = bme280.bme280.measure_alti()

            gm.tele2_env['temperature'] = gm.env['temp']
            gm.tele2_env['humidity'] = gm.env['humi']
            gm.tele2_env['pressure'] = gm.env['pres']
            gm.tele2_env['cpu_temperature'] = gm.status['cpu_temp']

            # if cnt < 3:
            #     mylog.debug('fun7_bme280 test: ' + str(gm.env))
            # elif cnt == 3:
            #     pass
            # else:
            #     pass

            cnt += 1
            time.sleep(1)
            pass

    th7 = threading.Thread(target=th_fun7_bme280, daemon=True, args=(2,))
    th7.start()

    def th_fun8_iot_server(arg1):
        """publish to MQTT Broker"""
        cnt = 0
        while True:
            data = json.dumps(gm.tele2_env)
            try:
                response = requests.post(things1, headers=things_headers, data=data)
            except:
                mylog.error('things1 request fail')

            cnt += 1
            time.sleep(2)

    th8 = threading.Thread(target=th_fun8_iot_server, daemon=True, args=(2,))
    th8.start()

    def th_fun9(arg1):
        """change neopixel led color"""

        gm.status['thread']['led'] = True

        cnt = 0
        while True:
            # mylog.info('ledcolor running...')
            # ledcolor.ledcolor.hello()

            if cnt % 3 == 0:
                led.ledcolor.color_green()
            elif cnt % 3 == 1:
                led.ledcolor.color_red()
            else:
                led.ledcolor.color_blue()

            cnt += 1
            time.sleep(1)

    th9 = threading.Thread(target=th_fun9, daemon=True, args=(2,))
    th9.start()

    def th_fun12(arg1):
        """lte-m1 modem mqtt"""

        def print2(*s):
            if True:
                print(__name__, *s)

        gm.status['thread']['lte'] = True

        # dev1 = '/dev/ttyUSB0'
        # dev1 = 'COM16'
        if sys.platform == 'win32':
            dev1 = 'COM16'
        elif sys.platform == 'linux':
            dev1 = '/dev/ttyUSB1'
        elif sys.platform == 'cygwin':
            pass
        else:
            pass

        baud_rate = gm.cnfg['lte']['baud_rate']     # 115200  # 19200 # 9600
        time_out = gm.cnfg['lte']['time_out']

        print('modem opening...')
        modem = ModemMqtt()  # dev1, baudrate=baud_rate, timeout=time_out)
        print('config...')
        at_cmds = [
            'AT*WMQTCFG=endpoint,mqtt.gleeze.com',
            'AT*WMQTCFG=username,forall'
        ]
        modem.at_config(at_cmds, wait=0.5)  # 모뎀 부팅 후 한번만
        s1 = '''AT*WMQTPUB='''
        s2 = '''v1/devices/me/telemetry,'''

        cnt = 0
        while True:
            cnt += 1
            print('connecting...')
            modem.at_connect()  # 전송 전

            dic1 = {'value': cnt, 'host': gm.hostname}
            s3 = '\"' + str(dic1) + '\"'
            cmd = s1 + s2 + s3
            print2(cmd)

            print('sending...')
            modem.at_mqtt_pub(cmd)

            print('disconnecting...')
            modem.at_disconnect()  # 전송 후

            # print('modem closing...')
            # modem.close()  # 프로그램 완전 종료 시에만 호출하라

            if cnt < 2:  # 처음에만 자주 전송한다.
                time.sleep(10)
            elif cnt == 2:
                print('next time, lte send_interval will be change to:', gm.cnfg['lte']['send_interval'])
            else:
                time.sleep(gm.cnfg['lte']['send_interval'])

    th12 = threading.Thread(target=th_fun12, daemon=True, args=(2,))
    th12.start()

