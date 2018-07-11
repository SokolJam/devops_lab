from datetime import datetime
import json
import logging
import settings
import sys
import time


import psutil


logging.basicConfig(format='TIMESTAMP: %(asctime)s: %(message)s', level=logging.INFO,
                    filename=settings.OUTPUT_FILE, filemode='w+')


data = []


def write_json(**kwargs):
    data.append({'TIMESTAMP': datetime.now().strftime('%d-%m-%Y_%H-%M-%S'),
                 'SNAPSHOT': kwargs['i'], 'Overall CPU load (%)': kwargs['cp'],
                 'Free SWAP memory (M)': kwargs['s_m'],
                 'Used virtual memory (%)': kwargs['v_m'],
                 'IO information': {'read': kwargs['r_io'], 'write': kwargs['w_io']},
                 'Network information': {'packet_sent': kwargs['net1'],
                                         'packet_recv': kwargs['net2']}})

    with open(settings.OUTPUT_JSON, 'w') as js:
        json.dump(data, js)


def log(**kwargs):
    logging.info('SNAPSHOT {i}: Overall CPU load = {cp} % : Free SWAP memory = '
                 '{s_m} M: Used virtual memory = {v_m} % : IO information read = '
                 '{r_io} write = {w_io} : Network information packet_sent = {net1} '
                 'packet_recv = {net2}'.format(cp=kwargs['cp'], s_m=kwargs['s_m'],
                                               v_m=kwargs['v_m'], r_io=kwargs['r_io'],
                                               w_io=kwargs['w_io'], net1=kwargs['net1'],
                                               net2=kwargs['net2'], i=kwargs['i']))


def info(i):
    dict_choose = {'txt': log, 'json': write_json}
    cpu = psutil.cpu_percent(interval=1)
    swap_mem = int(psutil.swap_memory()[2] / (2 ** 20))
    v_mem = psutil.virtual_memory()[2]
    r_io = psutil.disk_io_counters().read_count
    w_io = psutil.disk_io_counters().write_count
    net1 = psutil.net_io_counters().packets_sent
    net2 = psutil.net_io_counters().packets_recv

    dict_choose[settings.OUTPUT](cp=cpu, s_m=swap_mem, v_m=v_mem, r_io=r_io, w_io=w_io,
                                 net1=net1, net2=net2, i=i)


if __name__ == '__main__':
    try:
        logging.info('---Monitoring is started!---')
        print('{time} ---Monitoring is started!---'
              '\nOutput to file: '
              '{file}'.format(time=datetime.now().strftime('%d-%m-%Y_%H-%M-%S'),
                              file=settings.OUTPUT_FILE))
        index = 1
        while True:
            info(index)
            time.sleep(settings.INTERVAL)
            index += 1
    except KeyboardInterrupt:
        logging.info('---Monitoring is stopped!---')
        print('{time} ---Monitoring is stopped!---'
              ''.format(time=datetime.now().strftime('%d-%m-%Y_%H-%M-%S')))
        sys.exit()
